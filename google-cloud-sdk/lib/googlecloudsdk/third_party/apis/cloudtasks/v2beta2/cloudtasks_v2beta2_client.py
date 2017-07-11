"""Generated client library for cloudtasks version v2beta2."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudtasks.v2beta2 import cloudtasks_v2beta2_messages as messages


class CloudtasksV2beta2(base_api.BaseApiClient):
  """Generated client library for service cloudtasks version v2beta2."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudtasks.googleapis.com/'

  _PACKAGE = u'cloudtasks'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v2beta2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudtasksV2beta2'
  _URL_VERSION = u'v2beta2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new cloudtasks handle."""
    url = url or self.BASE_URL
    super(CloudtasksV2beta2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_locations_queues_tasks = self.ProjectsLocationsQueuesTasksService(self)
    self.projects_locations_queues = self.ProjectsLocationsQueuesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsQueuesTasksService(base_api.BaseApiService):
    """Service class for the projects_locations_queues_tasks resource."""

    _NAME = u'projects_locations_queues_tasks'

    def __init__(self, client):
      super(CloudtasksV2beta2.ProjectsLocationsQueuesTasksService, self).__init__(client)
      self._upload_configs = {
          }

    def Acknowledge(self, request, global_params=None):
      """Acknowledges a pull task.

The lease holder, that is, the entity that received this task in
a PullTasksResponse, must call this method to indicate that
the work associated with the task has finished.

The lease holder must acknowledge a task within the
PullTasksRequest.lease_duration or the lease will expire and
the task will become ready to be returned in a different
PullTasksResponse. After the task is acknowledged, it will
not be returned by a later CloudTasks.PullTasks,
CloudTasks.GetTask, or CloudTasks.ListTasks.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksAcknowledgeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Acknowledge')
      return self._RunMethod(
          config, request, global_params=global_params)

    Acknowledge.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}:acknowledge',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.acknowledge',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:acknowledge',
        request_field=u'acknowledgeTaskRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksAcknowledgeRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def CancelLease(self, request, global_params=None):
      """Cancel a pull task's lease.

The lease holder can use this method to cancel a task's lease
by setting Task.schedule_time to now. This will make the task
available to be leased to the next caller of CloudTasks.PullTasks.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksCancelLeaseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Task) The response message.
      """
      config = self.GetMethodConfig('CancelLease')
      return self._RunMethod(
          config, request, global_params=global_params)

    CancelLease.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}:cancelLease',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.cancelLease',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:cancelLease',
        request_field=u'cancelLeaseRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksCancelLeaseRequest',
        response_type_name=u'Task',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      """Creates a task and adds it to a queue.

To add multiple tasks at the same time, use
[HTTP batching](https://cloud.google.com/storage/docs/json_api/v1/how-tos/batch)
or the batching documentation for your client library, for example
https://developers.google.com/api-client-library/python/guide/batch.

Tasks cannot be updated after creation; there is no UpdateTask command.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Task) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v2beta2/{+parent}/tasks',
        request_field=u'createTaskRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksCreateRequest',
        response_type_name=u'Task',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a task.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}',
        http_method=u'DELETE',
        method_id=u'cloudtasks.projects.locations.queues.tasks.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets a task.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Task) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}',
        http_method=u'GET',
        method_id=u'cloudtasks.projects.locations.queues.tasks.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'responseView'],
        relative_path=u'v2beta2/{+name}',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksGetRequest',
        response_type_name=u'Task',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists the tasks in a queue.

By default response_view is Task.View.BASIC; not all
information is retrieved by default due to performance
considerations; ListTasksRequest.response_view controls the
subset of information which is returned.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTasksResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks',
        http_method=u'GET',
        method_id=u'cloudtasks.projects.locations.queues.tasks.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'orderBy', u'pageSize', u'pageToken', u'responseView'],
        relative_path=u'v2beta2/{+parent}/tasks',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksListRequest',
        response_type_name=u'ListTasksResponse',
        supports_download=False,
    )

    def Pull(self, request, global_params=None):
      """Pulls tasks from a pull queue and acquires a lease on them for a.
specified PullTasksRequest.lease_duration.

This method is invoked by the lease holder to obtain the
lease. The lease holder must acknowledge the task via
CloudTasks.AcknowledgeTask after they have performed the work
associated with the task.

The payload is intended to store data that the lease holder needs
to perform the work associated with the task. To return the
payloads in the PullTasksResponse, set
PullTasksRequest.response_view to FULL.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksPullRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PullTasksResponse) The response message.
      """
      config = self.GetMethodConfig('Pull')
      return self._RunMethod(
          config, request, global_params=global_params)

    Pull.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks:pull',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.pull',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}/tasks:pull',
        request_field=u'pullTasksRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksPullRequest',
        response_type_name=u'PullTasksResponse',
        supports_download=False,
    )

    def RenewLease(self, request, global_params=None):
      """Renew the current lease of a pull task.

The lease holder can use this method to extend the lease by a new
duration, starting from now. The new task lease will be
returned in Task.schedule_time.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksRenewLeaseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Task) The response message.
      """
      config = self.GetMethodConfig('RenewLease')
      return self._RunMethod(
          config, request, global_params=global_params)

    RenewLease.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}:renewLease',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.renewLease',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:renewLease',
        request_field=u'renewLeaseRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksRenewLeaseRequest',
        response_type_name=u'Task',
        supports_download=False,
    )

  class ProjectsLocationsQueuesService(base_api.BaseApiService):
    """Service class for the projects_locations_queues resource."""

    _NAME = u'projects_locations_queues'

    def __init__(self, client):
      super(CloudtasksV2beta2.ProjectsLocationsQueuesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets a queue.

      Args:
        request: (CloudtasksProjectsLocationsQueuesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Queue) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}',
        http_method=u'GET',
        method_id=u'cloudtasks.projects.locations.queues.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesGetRequest',
        response_type_name=u'Queue',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists queues.

Queues are returned in lexicographical order.

      Args:
        request: (CloudtasksProjectsLocationsQueuesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListQueuesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues',
        http_method=u'GET',
        method_id=u'cloudtasks.projects.locations.queues.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v2beta2/{+parent}/queues',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesListRequest',
        response_type_name=u'ListQueuesResponse',
        supports_download=False,
    )

    def Purge(self, request, global_params=None):
      """Purges a queue by deleting all of its tasks.

Purge operations can take up to one minute to take effect. Tasks
might be dispatched before the purge takes effect. A purge is irreversible.

Note: this command purges all tasks that were created five
minutes or more before now.

      Args:
        request: (CloudtasksProjectsLocationsQueuesPurgeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Queue) The response message.
      """
      config = self.GetMethodConfig('Purge')
      return self._RunMethod(
          config, request, global_params=global_params)

    Purge.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}:purge',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.purge',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:purge',
        request_field=u'purgeQueueRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesPurgeRequest',
        response_type_name=u'Queue',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(CloudtasksV2beta2.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(CloudtasksV2beta2.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
