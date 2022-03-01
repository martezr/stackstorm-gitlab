import time

from lib import action


class TriggerProjectPipelineAction(action.GitlabBaseAction):
    def run(self, project, ref, trigger_token, variables):
        project_payload = self.gitlab.projects.get(project)
        pipeline = project_payload.trigger_pipeline(ref,trigger_token, variables=variables)
        while pipeline.finished_at is None:
            pipeline.refresh()
            time.sleep(10)
        return pipeline