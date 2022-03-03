from lib import action


class CloseProjectIssueAction(action.GitlabBaseAction):
    def run(self, project, issue_iid, credentials, url, token, verify_ssl):
        self.get_client(credentials, url, token, verify_ssl)
        project_payload = self.gitlab.projects.get(project)
        issue_payload = project_payload.issues.get(issue_iid)
        issue_payload.state_event = 'close'
        issue_payload.save()
        return issue_payload.attributes