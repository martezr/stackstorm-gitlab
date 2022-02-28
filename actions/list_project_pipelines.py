from lib import action


class ListProjectPipelinesAction(action.GitlabBaseAction):
    def run(self, project, issue_iid):
        project_payload = self.gitlab.projects.get(project)
        pipelines_payload = project_payload.pipelines.list()
        return pipelines_payload.attributes