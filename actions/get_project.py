from lib import action


class GitlabProject(action.GitlabBaseAction):
    def run(self, project):
        project_payload = self.gitlab.projects.get(project)
        return project_payload.attributes