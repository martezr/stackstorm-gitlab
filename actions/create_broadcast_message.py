from lib import action


class CreateBroadcastMessageAction(action.GitlabBaseAction):
    def run(self, message, credentials, url, token, verify_ssl):
        self.get_client(credentials, url, token, verify_ssl)
        msg = self.gitlab.broadcastmessages.create({'message': message})
        return msg