from lib import action


class GetProjectBranchAction(action.GitlabBaseAction):
    def run(self, project, branch, credentials, url, token, verify_ssl):
        self.get_client(credentials, url, token, verify_ssl)
        project_payload = self.gitlab.projects.get(project)
        found_branch = project_payload.branches.get(branch)
        return found_branch.attributes