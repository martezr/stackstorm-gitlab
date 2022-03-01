import time

from lib import action


class TriggerProjectPipelineAction(action.GitlabBaseAction):
    def run(self, project, trigger_token):
        project_payload = self.gitlab.projects.get(project)
        pipeline = project_payload.trigger_pipeline('main',trigger_token, variables={})
        while pipeline.finished_at is None:
            pipeline.refresh()
            time.sleep(10)
        return pipeline