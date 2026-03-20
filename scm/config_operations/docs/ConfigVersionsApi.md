# scm.config_operations.ConfigVersionsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/operations/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_candidate_config_versions**](ConfigVersionsApi.md#delete_candidate_config_versions) | **DELETE** /config-versions/candidate | Delete a candidate configuration
[**get_config_versions_by_id**](ConfigVersionsApi.md#get_config_versions_by_id) | **GET** /config-versions/{version} | Get config by version
[**get_running_config_versions**](ConfigVersionsApi.md#get_running_config_versions) | **GET** /config-versions/running | Get running configuration versions
[**list_config_versions**](ConfigVersionsApi.md#list_config_versions) | **GET** /config-versions | List configuration versions
[**load_config_versions**](ConfigVersionsApi.md#load_config_versions) | **POST** /config-versions:load | Load config version
[**push_candidate_config_versions**](ConfigVersionsApi.md#push_candidate_config_versions) | **POST** /config-versions/candidate:push | Push the candidate configuration


# **delete_candidate_config_versions**
> delete_candidate_config_versions()

Delete a candidate configuration

Delete a candidate configuration.  Roll back to the running configuration. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_operations
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
    api_instance = scm.config_operations.ConfigVersionsApi(api_client)

    try:
        # Delete a candidate configuration
        api_instance.delete_candidate_config_versions()
    except Exception as e:
        print("Exception when calling ConfigVersionsApi->delete_candidate_config_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

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
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_versions_by_id**
> List[ConfigVersion] get_config_versions_by_id(version)

Get config by version

Get config by version. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_operations
from scm.config_operations.models.config_version import ConfigVersion
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
    api_instance = scm.config_operations.ConfigVersionsApi(api_client)
    version = 56 # int | The configuration version number

    try:
        # Get config by version
        api_response = api_instance.get_config_versions_by_id(version)
        print("The response of ConfigVersionsApi->get_config_versions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigVersionsApi->get_config_versions_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **int**| The configuration version number | 

### Return type

[**List[ConfigVersion]**](ConfigVersion.md)

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

# **get_running_config_versions**
> RunningConfigVersionsResponse get_running_config_versions()

Get running configuration versions

Get the running configuration versions on each folder. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_operations
from scm.config_operations.models.running_config_versions_response import RunningConfigVersionsResponse
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
    api_instance = scm.config_operations.ConfigVersionsApi(api_client)

    try:
        # Get running configuration versions
        api_response = api_instance.get_running_config_versions()
        print("The response of ConfigVersionsApi->get_running_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigVersionsApi->get_running_config_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RunningConfigVersionsResponse**](RunningConfigVersionsResponse.md)

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

# **list_config_versions**
> ConfigVersionsListResponse list_config_versions(limit=limit, offset=offset)

List configuration versions

Retrieve a list of configuration versions. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_operations
from scm.config_operations.models.config_versions_list_response import ConfigVersionsListResponse
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
    api_instance = scm.config_operations.ConfigVersionsApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List configuration versions
        api_response = api_instance.list_config_versions(limit=limit, offset=offset)
        print("The response of ConfigVersionsApi->list_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigVersionsApi->list_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]

### Return type

[**ConfigVersionsListResponse**](ConfigVersionsListResponse.md)

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

# **load_config_versions**
> load_config_versions(load_config=load_config)

Load config version

Load a specific configuration version into the candidate configuration. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_operations
from scm.config_operations.models.load_config import LoadConfig
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
    api_instance = scm.config_operations.ConfigVersionsApi(api_client)
    load_config = scm.config_operations.LoadConfig() # LoadConfig | Created (optional)

    try:
        # Load config version
        api_instance.load_config_versions(load_config=load_config)
    except Exception as e:
        print("Exception when calling ConfigVersionsApi->load_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_config** | [**LoadConfig**](LoadConfig.md)| Created | [optional] 

### Return type

void (empty response body)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **push_candidate_config_versions**
> push_candidate_config_versions(push_candidate_config_versions_request=push_candidate_config_versions_request)

Push the candidate configuration

Push the candidate configuration. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_operations
from scm.config_operations.models.push_candidate_config_versions_request import PushCandidateConfigVersionsRequest
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
    api_instance = scm.config_operations.ConfigVersionsApi(api_client)
    push_candidate_config_versions_request = scm.config_operations.PushCandidateConfigVersionsRequest() # PushCandidateConfigVersionsRequest | Created (optional)

    try:
        # Push the candidate configuration
        api_instance.push_candidate_config_versions(push_candidate_config_versions_request=push_candidate_config_versions_request)
    except Exception as e:
        print("Exception when calling ConfigVersionsApi->push_candidate_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_candidate_config_versions_request** | [**PushCandidateConfigVersionsRequest**](PushCandidateConfigVersionsRequest.md)| Created | [optional] 

### Return type

void (empty response body)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

