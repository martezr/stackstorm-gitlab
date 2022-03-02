import gitlab
import urllib3

from st2common.runners.base_action import Action

urllib3.disable_warnings()

class GitlabBaseAction(Action):
    def __init__(self, config):
        super(GitlabBaseAction, self).__init__(config)
        self.gitlab = self._get_client()

    def config_override(self, new_config):
        self.config = new_config
        self.gitlab = self._get_client()

    def _get_client(self):
        url = self.config['url']
        try:
            token = self.config['token']
        except KeyError:
            token = None
        try:
            verify_ssl = self.config['verify_ssl']
        except KeyError:
            verify_ssl = None

        client = gitlab.Gitlab(url=url, private_token=token, ssl_verify=verify_ssl)
        return client