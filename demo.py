import gitlab
import json
import urllib3


urllib3.disable_warnings()

url="https://grtmanage01.grt.local"
token="sw-mYxD4WX3ScZ99J53n"
verify_ssl=False

client = gitlab.Gitlab(url=url, private_token=token, ssl_verify=verify_ssl)
project = client.projects.get("grt/ansibledemo")
pipeline = project.trigger_pipeline('master','960858c208a81c73b2676ffba60983',variables={"FOO": 'bar'})
print(pipeline)