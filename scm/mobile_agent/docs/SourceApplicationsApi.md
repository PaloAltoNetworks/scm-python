# scm.mobile_agent.SourceApplicationsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/mobile-agent/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_protect_source_application**](SourceApplicationsApi.md#create_global_protect_source_application) | **POST** /forwarding-profile-source-applications | Create a GlobalProtect source application
[**delete_global_protect_source_application**](SourceApplicationsApi.md#delete_global_protect_source_application) | **DELETE** /forwarding-profile-source-applications/{id} | Delete a GlobalProtect source application
[**get_global_protect_source_application_by_id**](SourceApplicationsApi.md#get_global_protect_source_application_by_id) | **GET** /forwarding-profile-source-applications/{id} | Get a GlobalProtect source application
[**list_global_protect_source_applications**](SourceApplicationsApi.md#list_global_protect_source_applications) | **GET** /forwarding-profile-source-applications | List GlobalProtect source applications
[**update_global_protect_source_application_by_id**](SourceApplicationsApi.md#update_global_protect_source_application_by_id) | **PUT** /forwarding-profile-source-applications/{id} | Update a GlobalProtect source application


# **create_global_protect_source_application**
> ForwardingProfileSourceApplications create_global_protect_source_application(folder=folder, forwarding_profile_source_applications=forwarding_profile_source_applications)

Create a GlobalProtect source application

Create a new GlobalProtect source application 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_source_applications import ForwardingProfileSourceApplications
from scm.mobile_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.mobile_agent.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/mobile-agent/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.mobile_agent.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.mobile_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.mobile_agent.SourceApplicationsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    forwarding_profile_source_applications = scm.mobile_agent.ForwardingProfileSourceApplications() # ForwardingProfileSourceApplications | Created (optional)

    try:
        # Create a GlobalProtect source application
        api_response = api_instance.create_global_protect_source_application(folder=folder, forwarding_profile_source_applications=forwarding_profile_source_applications)
        print("The response of SourceApplicationsApi->create_global_protect_source_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApplicationsApi->create_global_protect_source_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **forwarding_profile_source_applications** | [**ForwardingProfileSourceApplications**](ForwardingProfileSourceApplications.md)| Created | [optional] 

### Return type

[**ForwardingProfileSourceApplications**](ForwardingProfileSourceApplications.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_global_protect_source_application**
> delete_global_protect_source_application(id)

Delete a GlobalProtect source application

Delete a GlobalProtect source application 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.mobile_agent.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/mobile-agent/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.mobile_agent.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.mobile_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.mobile_agent.SourceApplicationsApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Delete a GlobalProtect source application
        api_instance.delete_global_protect_source_application(id)
    except Exception as e:
        print("Exception when calling SourceApplicationsApi->delete_global_protect_source_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

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

# **get_global_protect_source_application_by_id**
> ForwardingProfileSourceApplications get_global_protect_source_application_by_id(id)

Get a GlobalProtect source application

Retrieve an existing GlobalProtect source application 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_source_applications import ForwardingProfileSourceApplications
from scm.mobile_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.mobile_agent.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/mobile-agent/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.mobile_agent.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.mobile_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.mobile_agent.SourceApplicationsApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get a GlobalProtect source application
        api_response = api_instance.get_global_protect_source_application_by_id(id)
        print("The response of SourceApplicationsApi->get_global_protect_source_application_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApplicationsApi->get_global_protect_source_application_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**ForwardingProfileSourceApplications**](ForwardingProfileSourceApplications.md)

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

# **list_global_protect_source_applications**
> GlobalProtectSourceApplicationsListResponse list_global_protect_source_applications(name=name, limit=limit, offset=offset, folder=folder)

List GlobalProtect source applications

Retrieve a list of GlobalProtect source applications 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.global_protect_source_applications_list_response import GlobalProtectSourceApplicationsListResponse
from scm.mobile_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.mobile_agent.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/mobile-agent/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.mobile_agent.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.mobile_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.mobile_agent.SourceApplicationsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)

    try:
        # List GlobalProtect source applications
        api_response = api_instance.list_global_protect_source_applications(name=name, limit=limit, offset=offset, folder=folder)
        print("The response of SourceApplicationsApi->list_global_protect_source_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApplicationsApi->list_global_protect_source_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **folder** | **str**| The folder in which the resource is defined  | [optional] 

### Return type

[**GlobalProtectSourceApplicationsListResponse**](GlobalProtectSourceApplicationsListResponse.md)

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

# **update_global_protect_source_application_by_id**
> ForwardingProfileSourceApplications update_global_protect_source_application_by_id(id, forwarding_profile_source_applications=forwarding_profile_source_applications)

Update a GlobalProtect source application

Update an existing GlobalProtect source application 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_source_applications import ForwardingProfileSourceApplications
from scm.mobile_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.mobile_agent.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/mobile-agent/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.mobile_agent.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.mobile_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.mobile_agent.SourceApplicationsApi(api_client)
    id = 'id_example' # str | The UUID of the resource
    forwarding_profile_source_applications = scm.mobile_agent.ForwardingProfileSourceApplications() # ForwardingProfileSourceApplications | The source application resource definition (optional)

    try:
        # Update a GlobalProtect source application
        api_response = api_instance.update_global_protect_source_application_by_id(id, forwarding_profile_source_applications=forwarding_profile_source_applications)
        print("The response of SourceApplicationsApi->update_global_protect_source_application_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApplicationsApi->update_global_protect_source_application_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 
 **forwarding_profile_source_applications** | [**ForwardingProfileSourceApplications**](ForwardingProfileSourceApplications.md)| The source application resource definition | [optional] 

### Return type

[**ForwardingProfileSourceApplications**](ForwardingProfileSourceApplications.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
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

