from lib import action


class GetProjectAction(action.GitlabBaseAction):
    def run(self, project, credentials, url, token, verify_ssl):
        self.get_client(credentials, url, token, verify_ssl)
        project_payload = self.gitlab.projects.get(project)
        return project_payload.attributes