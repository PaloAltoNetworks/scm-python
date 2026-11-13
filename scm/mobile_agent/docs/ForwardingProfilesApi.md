# scm.mobile_agent.ForwardingProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/mobile-agent/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_protect_forwarding_profile**](ForwardingProfilesApi.md#create_global_protect_forwarding_profile) | **POST** /forwarding-profiles | Create a GlobalProtect forwarding profile
[**delete_global_protect_forwarding_profile**](ForwardingProfilesApi.md#delete_global_protect_forwarding_profile) | **DELETE** /forwarding-profiles/{id} | Delete a GlobalProtect forwarding profile
[**get_global_protect_forwarding_profile_by_id**](ForwardingProfilesApi.md#get_global_protect_forwarding_profile_by_id) | **GET** /forwarding-profiles/{id} | Get a GlobalProtect forwarding profile
[**list_global_protect_forwarding_profiles**](ForwardingProfilesApi.md#list_global_protect_forwarding_profiles) | **GET** /forwarding-profiles | List GlobalProtect forwarding profiles
[**update_global_protect_forwarding_profile_by_id**](ForwardingProfilesApi.md#update_global_protect_forwarding_profile_by_id) | **PUT** /forwarding-profiles/{id} | Update a GlobalProtect forwarding profile


# **create_global_protect_forwarding_profile**
> ForwardingProfiles create_global_protect_forwarding_profile(folder=folder, forwarding_profiles=forwarding_profiles)

Create a GlobalProtect forwarding profile

Create a new GlobalProtect forwarding profile 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profiles import ForwardingProfiles
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
    api_instance = scm.mobile_agent.ForwardingProfilesApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    forwarding_profiles = scm.mobile_agent.ForwardingProfiles() # ForwardingProfiles | Created (optional)

    try:
        # Create a GlobalProtect forwarding profile
        api_response = api_instance.create_global_protect_forwarding_profile(folder=folder, forwarding_profiles=forwarding_profiles)
        print("The response of ForwardingProfilesApi->create_global_protect_forwarding_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardingProfilesApi->create_global_protect_forwarding_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **forwarding_profiles** | [**ForwardingProfiles**](ForwardingProfiles.md)| Created | [optional] 

### Return type

[**ForwardingProfiles**](ForwardingProfiles.md)

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

# **delete_global_protect_forwarding_profile**
> delete_global_protect_forwarding_profile(id)

Delete a GlobalProtect forwarding profile

Delete a GlobalProtect forwarding profile 

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
    api_instance = scm.mobile_agent.ForwardingProfilesApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Delete a GlobalProtect forwarding profile
        api_instance.delete_global_protect_forwarding_profile(id)
    except Exception as e:
        print("Exception when calling ForwardingProfilesApi->delete_global_protect_forwarding_profile: %s\n" % e)
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

# **get_global_protect_forwarding_profile_by_id**
> ForwardingProfiles get_global_protect_forwarding_profile_by_id(id)

Get a GlobalProtect forwarding profile

Retrieve an existing GlobalProtect forwarding profile 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profiles import ForwardingProfiles
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
    api_instance = scm.mobile_agent.ForwardingProfilesApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get a GlobalProtect forwarding profile
        api_response = api_instance.get_global_protect_forwarding_profile_by_id(id)
        print("The response of ForwardingProfilesApi->get_global_protect_forwarding_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardingProfilesApi->get_global_protect_forwarding_profile_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**ForwardingProfiles**](ForwardingProfiles.md)

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

# **list_global_protect_forwarding_profiles**
> GlobalProtectForwardingProfilesListResponse list_global_protect_forwarding_profiles(name=name, limit=limit, offset=offset, folder=folder)

List GlobalProtect forwarding profiles

Retrieve a list of GlobalProtect forwarding profiles 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.global_protect_forwarding_profiles_list_response import GlobalProtectForwardingProfilesListResponse
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
    api_instance = scm.mobile_agent.ForwardingProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)

    try:
        # List GlobalProtect forwarding profiles
        api_response = api_instance.list_global_protect_forwarding_profiles(name=name, limit=limit, offset=offset, folder=folder)
        print("The response of ForwardingProfilesApi->list_global_protect_forwarding_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardingProfilesApi->list_global_protect_forwarding_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **folder** | **str**| The folder in which the resource is defined  | [optional] 

### Return type

[**GlobalProtectForwardingProfilesListResponse**](GlobalProtectForwardingProfilesListResponse.md)

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

# **update_global_protect_forwarding_profile_by_id**
> ForwardingProfiles update_global_protect_forwarding_profile_by_id(id, forwarding_profiles=forwarding_profiles)

Update a GlobalProtect forwarding profile

Update an existing GlobalProtect forwarding profile 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profiles import ForwardingProfiles
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
    api_instance = scm.mobile_agent.ForwardingProfilesApi(api_client)
    id = 'id_example' # str | The UUID of the resource
    forwarding_profiles = scm.mobile_agent.ForwardingProfiles() # ForwardingProfiles | The forwarding profile resource definition (optional)

    try:
        # Update a GlobalProtect forwarding profile
        api_response = api_instance.update_global_protect_forwarding_profile_by_id(id, forwarding_profiles=forwarding_profiles)
        print("The response of ForwardingProfilesApi->update_global_protect_forwarding_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardingProfilesApi->update_global_protect_forwarding_profile_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 
 **forwarding_profiles** | [**ForwardingProfiles**](ForwardingProfiles.md)| The forwarding profile resource definition | [optional] 

### Return type

[**ForwardingProfiles**](ForwardingProfiles.md)

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

