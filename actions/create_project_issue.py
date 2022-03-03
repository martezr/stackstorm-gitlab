from lib import action


class CreateProjectIssueAction(action.GitlabBaseAction):
    def run(self, project, title, description, credentials, url, token, verify_ssl):
        self.get_client(credentials, url, token, verify_ssl)
        project_payload = self.gitlab.projects.get(project)
        issue_payload = project_payload.issues.create({'title': title,
                               'description': description})

        return issue_payload.attributes