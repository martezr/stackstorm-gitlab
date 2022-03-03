from lib import action


class ListProjectBranchesAction(action.GitlabBaseAction):
    def run(self, project, credentials, url, token, verify_ssl):
        self.get_client(credentials, url, token, verify_ssl)
        project_payload = self.gitlab.projects.get(project)
        branches = project_payload.branches.list()
        branches_payload = []
        for branch in branches:
            branches_payload.append(branch.attributes)
        return branches_payload