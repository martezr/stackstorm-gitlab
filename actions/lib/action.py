import gitlab
import urllib3

from st2common.runners.base_action import Action

urllib3.disable_warnings()

CONNECTION_ITEMS = ['url', 'token', 'verify_ssl']

class GitlabBaseAction(Action):
    def __init__(self, config):
        super(GitlabBaseAction, self).__init__(config)
        if config is None:
            raise ValueError("No connection configuration details found")
        if "gitlabinstance" in config:
            if config['gitlabinstance'] is None:
                raise ValueError("'gitlabinstance' config defined but empty.")
            else:
                pass
        else:
            raise ValueError("No connection configuration details found")

    def config_override(self, new_config):
        self.config = new_config
        self.gitlab = self._get_client()

    def _get_connection_info(self, gitlabinstance):
        if gitlabinstance:
            connection = self.config['gitlabinstance'].get(gitlabinstance)
        else:
            connection = self.config['gitlabinstance'].get('default')

        for item in CONNECTION_ITEMS:
            if item in connection:
                pass
            else:
                raise KeyError("gitlab.yaml Mising: gitlabinstance:%s:%s"
                               % (gitlabinstance, item))

        return connection

    def get_client(self, gitlabinstance):
        connection = self._get_connection_info(gitlabinstance)
        url = connection['url']
        try:
            token = connection['token']
        except KeyError:
            token = None
        try:
            verify_ssl = connection['verify_ssl']
        except KeyError:
            verify_ssl = None

        client = gitlab.Gitlab(url=url, private_token=token, ssl_verify=verify_ssl)
        return client