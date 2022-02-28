from lib import action


class GitlabProject(action.GitlabBaseAction):
    def run(self, project):
        return self.gl.projects.get(project)
