from lib import action


class CreateProjectBranchAction(action.GitlabBaseAction):
    def run(self, project, branch, ref, credentials, url, token, verify_ssl):
        self.get_client(credentials, url, token, verify_ssl)
        project_payload = self.gitlab.projects.get(project)
        found_branch = project_payload.branches.create({'branch': branch,
                                  'ref': ref})
        return found_branch.attributes