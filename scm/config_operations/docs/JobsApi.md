# scm.config_operations.JobsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/operations/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_jobs_by_id**](JobsApi.md#get_jobs_by_id) | **GET** /jobs/{id} | Get a job
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /jobs | List jobs


# **get_jobs_by_id**
> JobsResponse get_jobs_by_id(id)

Get a job

Get an existing configuration job. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_operations
from scm.config_operations.models.jobs_response import JobsResponse
from scm.config_operations.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/operations/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_operations.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/operations/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_operations.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_operations.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_operations.JobsApi(api_client)
    id = 'id_example' # str | The ID of the job

    try:
        # Get a job
        api_response = api_instance.get_jobs_by_id(id)
        print("The response of JobsApi->get_jobs_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_jobs_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the job | 

### Return type

[**JobsResponse**](JobsResponse.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> JobsListResponse list_jobs()

List jobs

Retrieve a list of configuration jobs. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_operations
from scm.config_operations.models.jobs_list_response import JobsListResponse
from scm.config_operations.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/operations/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_operations.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/operations/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_operations.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_operations.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_operations.JobsApi(api_client)

    try:
        # List jobs
        api_response = api_instance.list_jobs()
        print("The response of JobsApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JobsListResponse**](JobsListResponse.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

