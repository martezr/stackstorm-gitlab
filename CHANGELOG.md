## v2.0.0

* Migrate the pack to use the python-gitlab library
* Add support for multiple Gitlab instances similar to the vSphere StackStorm pack

* The following actions have been renamed:

| Previous Action Name|New Action Name|
|------------|-------------------|
|`issue.info`|`get_project_issue`|
|`pipeline.list`|`list_project_pipelines`|
|`project.info`|`get_project`|
|`pipeline.trigger`|`trigger_project_pipeline`|


## v1.0.1

* Small bug fixes regarding Python 3 support

## v1.0.0

* Drop Python 2.7 support

## v0.5.5

  - Bump pack version 0.5.4 -> 0.5.5 to include changes in master not reflected in current version (Python 2.7/3.x compatibility)

## v0.5.2

  - Added new action: issue.info

## v0.5.0

  - API v4 support
  - actions and worklows renamed
