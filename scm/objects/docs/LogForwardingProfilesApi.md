# scm.objects.LogForwardingProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_forwarding_profiles**](LogForwardingProfilesApi.md#create_log_forwarding_profiles) | **POST** /log-forwarding-profiles | Create a log forwarding profile
[**delete_log_forwarding_profiles_by_id**](LogForwardingProfilesApi.md#delete_log_forwarding_profiles_by_id) | **DELETE** /log-forwarding-profiles/{id} | Delete a log forwarding profile
[**get_log_forwarding_profiles_by_id**](LogForwardingProfilesApi.md#get_log_forwarding_profiles_by_id) | **GET** /log-forwarding-profiles/{id} | Get a log forwarding profile
[**list_log_forwarding_profiles**](LogForwardingProfilesApi.md#list_log_forwarding_profiles) | **GET** /log-forwarding-profiles | List log forwarding profiles
[**update_log_forwarding_profiles_by_id**](LogForwardingProfilesApi.md#update_log_forwarding_profiles_by_id) | **PUT** /log-forwarding-profiles/{id} | Update a log forwarding profile


# **create_log_forwarding_profiles**
> LogForwardingProfiles create_log_forwarding_profiles(log_forwarding_profiles=log_forwarding_profiles)

Create a log forwarding profile

Create a new log forwarding profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.log_forwarding_profiles import LogForwardingProfiles
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.LogForwardingProfilesApi(api_client)
    log_forwarding_profiles = scm.objects.LogForwardingProfiles() # LogForwardingProfiles | Created (optional)

    try:
        # Create a log forwarding profile
        api_response = api_instance.create_log_forwarding_profiles(log_forwarding_profiles=log_forwarding_profiles)
        print("The response of LogForwardingProfilesApi->create_log_forwarding_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogForwardingProfilesApi->create_log_forwarding_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_forwarding_profiles** | [**LogForwardingProfiles**](LogForwardingProfiles.md)| Created | [optional] 

### Return type

[**LogForwardingProfiles**](LogForwardingProfiles.md)

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

# **delete_log_forwarding_profiles_by_id**
> delete_log_forwarding_profiles_by_id(id)

Delete a log forwarding profile

Delete a log forwarding profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.LogForwardingProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a log forwarding profile
        api_instance.delete_log_forwarding_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling LogForwardingProfilesApi->delete_log_forwarding_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

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

# **get_log_forwarding_profiles_by_id**
> LogForwardingProfiles get_log_forwarding_profiles_by_id(id)

Get a log forwarding profile

Get an existing log forwarding profile.

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.log_forwarding_profiles import LogForwardingProfiles
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.LogForwardingProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a log forwarding profile
        api_response = api_instance.get_log_forwarding_profiles_by_id(id)
        print("The response of LogForwardingProfilesApi->get_log_forwarding_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogForwardingProfilesApi->get_log_forwarding_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**LogForwardingProfiles**](LogForwardingProfiles.md)

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

# **list_log_forwarding_profiles**
> LogForwardingProfilesListResponse list_log_forwarding_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List log forwarding profiles

Retrieve a list of log forwarding profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.log_forwarding_profiles_list_response import LogForwardingProfilesListResponse
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.LogForwardingProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List log forwarding profiles
        api_response = api_instance.list_log_forwarding_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of LogForwardingProfilesApi->list_log_forwarding_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogForwardingProfilesApi->list_log_forwarding_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]

### Return type

[**LogForwardingProfilesListResponse**](LogForwardingProfilesListResponse.md)

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

# **update_log_forwarding_profiles_by_id**
> LogForwardingProfiles update_log_forwarding_profiles_by_id(id, log_forwarding_profiles=log_forwarding_profiles)

Update a log forwarding profile

Update an existing log forwarding profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.log_forwarding_profiles import LogForwardingProfiles
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.LogForwardingProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    log_forwarding_profiles = scm.objects.LogForwardingProfiles() # LogForwardingProfiles | OK (optional)

    try:
        # Update a log forwarding profile
        api_response = api_instance.update_log_forwarding_profiles_by_id(id, log_forwarding_profiles=log_forwarding_profiles)
        print("The response of LogForwardingProfilesApi->update_log_forwarding_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogForwardingProfilesApi->update_log_forwarding_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **log_forwarding_profiles** | [**LogForwardingProfiles**](LogForwardingProfiles.md)| OK | [optional] 

### Return type

[**LogForwardingProfiles**](LogForwardingProfiles.md)

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

