from lib import action


class GetProjectAction(action.GitlabBaseAction):
    def run(self, project, credentials):
        self.get_client(credentials)
        project_payload = self.projects.get(project)
        return project_payload.attributes