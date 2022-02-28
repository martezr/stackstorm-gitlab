from lib import action


class GitlabProjectIssue(action.GitlabBaseAction):
    def run(self, project, issue_iid):
        project_payload = self.gitlab.projects.get(project)
        issue_payload = project_payload.issues.get(issue_iid, lazy=True)
        return issue_payload.attributes