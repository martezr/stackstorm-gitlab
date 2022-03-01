from lib import action


class ListProjectPipelinesAction(action.GitlabBaseAction):
    def run(self, project):
        project_payload = self.gitlab.projects.get(project)
        pipelines_payload = project_payload.pipelines.list()
        pipelines_outpayload = []
        for pipeline in pipelines_payload:
            pipelines_outpayload.append(pipeline.attributes)
        return pipelines_outpayload