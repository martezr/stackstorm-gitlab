from lib import action


class DeleteProjectBranchAction(action.GitlabBaseAction):
    def run(self, project, branch, credentials, url, token, verify_ssl):
        self.get_client(credentials, url, token, verify_ssl)
        project_payload = self.gitlab.projects.get(project)
        return project_payload.branches.delete(branch)