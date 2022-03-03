from lib import action


class CreateProjectIssueAction(action.GitlabBaseAction):
    def run(self, project, credentials, url, token, verify_ssl):
        self.get_client(credentials, url, token, verify_ssl)
        project_payload = self.gitlab.projects.get(project)
        issue_payload = project_payload.issues.create({'title': 'I have a bug',
                               'description': 'Something useful here.'})

        return issue_payload.attributes