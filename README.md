# Gitlab Integration Pack

StackStorm integration pack for [GitLab](https://about.gitlab.com/).

# Quick Start

Install the pack

``` shell
st2 pack install gitlab
```

# Configuraton

The configuration for this pack is used to specify connection information for all Gitlab servers that StackStorm will connect to. The location for the config file is `/opt/stackstorm/configs/gitlab.yaml`. An example configuration located in the repo named [gitlab.yaml.example](./gitlab.yaml.example) can be copied to `/opt/stackstorm/configs/gitlab.yaml` and edited as required.

It should contain:

* `consul_profiles` - Mapping of name to an object containing Consul profile settings
  * `name` - Name of the consul profile
  * `url` - Consul server port. Default 8500
  * `token` - Consul API token
  * `verify` - Verify the SSL certificate for HTTPS requests. Default false (this option is ignored if ca_cert_path is supplied)


**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Schema Examples

```yaml
---
gitlabinstance:
  dev:
    url: username@dev.domain.tld
    token: xxx
    verify_ssl: false
  prod:
    url: username@test.domain.tld
    token: xxx
    verify_ssl: false

```

## Actions


The pack provides the following actions:

| Action Name | Description |
|-------------|-------------|
| create_project_issue | Create issue metadata |
| get_project_branch | Get a project branch |
| list_project_branches | List project branches |
| create_broadcast_message | Create broadcast message |
| delete_project_branch | Delete a project branch |
| create_project_branch | Create a project branch |
| close_project_issue | Get issue metadata |
| list_project_pipelines | List project pipelines |
| get_project_issue | Get issue metadata |
| get_project | Get project metadata |
| trigger_project_pipeline | Trigger a pipeline |


### Action Details

### create_project_issue
_Create issue metadata_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `project` | string | True | default | _The 'path_with_namespace' for the project that the issue lives in (group/group/project)_ |
| `title` | string | True | default | _The iid of the issue in the project (not global unique id) of the issue_ |
| `description` | string | True | default | _The iid of the issue in the project (not global unique id) of the issue_ |
| `credentials` | string | False | default | _The name of the project to fetch_ |
| `url` | string | False | default | _The name of the project to fetch_ |
| `token` | string | False | default | _The name of the project to fetch_ |
| `verify_ssl` | boolean | False | default | _The name of the project to fetch_ |
### get_project_branch
_Get a project branch_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `project` | string | True | default | _The name of the project the branch lives in_ |
| `branch` | string | True | default | _The name of the project branch to fetch_ |
| `credentials` | string | False | default | _The name of the project to fetch_ |
| `url` | string | False | default | _The name of the project to fetch_ |
| `token` | string | False | default | _The name of the project to fetch_ |
| `verify_ssl` | boolean | False | default | _The name of the project to fetch_ |
### list_project_branches
_List project branches_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `project` | string | True | default | _The name of the project to fetch_ |
| `credentials` | string | False | default | _The name of the project to fetch_ |
| `url` | string | False | default | _The name of the project to fetch_ |
| `token` | string | False | default | _The name of the project to fetch_ |
| `verify_ssl` | boolean | False | default | _The name of the project to fetch_ |
### create_broadcast_message
_Create broadcast message_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `message` | string | True | default | _The name of the project the branch lives in_ |
| `starts_at` | string | True | default | _The name of the project the branch lives in_ |
| `ends_at` | string | True | default | _The name of the project the branch lives in_ |
| `background_color` | string | True | default | _The name of the project the branch lives in_ |
| `credentials` | string | False | default | _The name of the project to fetch_ |
| `url` | string | False | default | _The name of the project to fetch_ |
| `token` | string | False | default | _The name of the project to fetch_ |
| `verify_ssl` | boolean | False | default | _The name of the project to fetch_ |
### delete_project_branch
_Delete a project branch_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `project` | string | True | default | _The name of the project the branch lives in_ |
| `branch` | string | True | default | _The name of the project branch to fetch_ |
| `credentials` | string | False | default | _The name of the project to fetch_ |
| `url` | string | False | default | _The name of the project to fetch_ |
| `token` | string | False | default | _The name of the project to fetch_ |
| `verify_ssl` | boolean | False | default | _The name of the project to fetch_ |
### create_project_branch
_Create a project branch_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `project` | string | True | default | _The name of the project the branch lives in_ |
| `branch` | string | True | default | _The name of the project branch to fetch_ |
| `ref` | string | True | default | _The name of the project branch to fetch_ |
| `credentials` | string | False | default | _The name of the project to fetch_ |
| `url` | string | False | default | _The name of the project to fetch_ |
| `token` | string | False | default | _The name of the project to fetch_ |
| `verify_ssl` | boolean | False | default | _The name of the project to fetch_ |
### close_project_issue
_Get issue metadata_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `project` | string | True | default | _The 'path_with_namespace' for the project that the issue lives in (group/group/project)_ |
| `issue_iid` | string | True | default | _The iid of the issue in the project (not global unique id) of the issue_ |
| `credentials` | string | False | default | _The name of the credentials to use for connecting to Gitlab_ |
| `url` | string | False | default | _The url of the Gitlab instance to override_ |
| `token` | string | False | default | _The name of the project to fetch_ |
| `verify_ssl` | boolean | False | default | _None_ |
### list_project_pipelines
_List project pipelines_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `project` | string | True | default | _The name of the project to fetch_ |
| `credentials` | string | False | default | _The name of the project to fetch_ |
| `url` | string | False | default | _The name of the project to fetch_ |
| `token` | string | False | default | _The name of the project to fetch_ |
| `verify_ssl` | boolean | False | default | _The name of the project to fetch_ |
### get_project_issue
_Get issue metadata_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `project` | string | True | default | _The 'path_with_namespace' for the project that the issue lives in (group/group/project)_ |
| `issue_iid` | string | True | default | _The iid of the issue in the project (not global unique id) of the issue_ |
| `credentials` | string | False | default | _The name of the project to fetch_ |
| `url` | string | False | default | _The name of the project to fetch_ |
| `token` | string | False | default | _The name of the project to fetch_ |
| `verify_ssl` | boolean | False | default | _The name of the project to fetch_ |
### get_project
_Get project metadata_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `project` | string | True | default | _The name of the project to fetch_ |
| `credentials` | string | False | default | _The name of the project to fetch_ |
| `url` | string | False | default | _The name of the project to fetch_ |
| `token` | string | False | default | _The name of the project to fetch_ |
| `verify_ssl` | boolean | False | default | _The name of the project to fetch_ |
### trigger_project_pipeline
_Trigger a pipeline_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `project` | string | True | default | _Unavailable_ |
| `ref` | string | True | default | _Unavailable_ |
| `trigger_token` | string | True | default | _CI Trigger Token_ |
| `variables` | object | default | default | _Pass variables to pipeline_ |



## Sensors

There are no sensors available for this pack.
