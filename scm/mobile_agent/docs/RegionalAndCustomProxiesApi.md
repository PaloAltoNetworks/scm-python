# scm.mobile_agent.RegionalAndCustomProxiesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/mobile-agent/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_protect_regional_and_custom_proxies**](RegionalAndCustomProxiesApi.md#create_global_protect_regional_and_custom_proxies) | **POST** /forwarding-profile-regional-and-custom-proxies | Create a GlobalProtect regional and custom proxy
[**delete_global_protect_regional_and_custom_proxies**](RegionalAndCustomProxiesApi.md#delete_global_protect_regional_and_custom_proxies) | **DELETE** /forwarding-profile-regional-and-custom-proxies/{id} | Delete a GlobalProtect regional and custom proxy
[**get_global_protect_regional_and_custom_proxy_by_id**](RegionalAndCustomProxiesApi.md#get_global_protect_regional_and_custom_proxy_by_id) | **GET** /forwarding-profile-regional-and-custom-proxies/{id} | Get a GlobalProtect regional and custom proxy
[**list_global_protect_regional_and_custom_proxies**](RegionalAndCustomProxiesApi.md#list_global_protect_regional_and_custom_proxies) | **GET** /forwarding-profile-regional-and-custom-proxies | List GlobalProtect regional and custom proxies
[**update_global_protect_regional_and_custom_proxy_by_id**](RegionalAndCustomProxiesApi.md#update_global_protect_regional_and_custom_proxy_by_id) | **PUT** /forwarding-profile-regional-and-custom-proxies/{id} | Update a GlobalProtect regional and custom proxy


# **create_global_protect_regional_and_custom_proxies**
> ForwardingProfileRegionalAndCustomProxies create_global_protect_regional_and_custom_proxies(folder=folder, forwarding_profile_regional_and_custom_proxies=forwarding_profile_regional_and_custom_proxies)

Create a GlobalProtect regional and custom proxy

Create a new GlobalProtect regional and custom proxy 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies import ForwardingProfileRegionalAndCustomProxies
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
    api_instance = scm.mobile_agent.RegionalAndCustomProxiesApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    forwarding_profile_regional_and_custom_proxies = scm.mobile_agent.ForwardingProfileRegionalAndCustomProxies() # ForwardingProfileRegionalAndCustomProxies | Created (optional)

    try:
        # Create a GlobalProtect regional and custom proxy
        api_response = api_instance.create_global_protect_regional_and_custom_proxies(folder=folder, forwarding_profile_regional_and_custom_proxies=forwarding_profile_regional_and_custom_proxies)
        print("The response of RegionalAndCustomProxiesApi->create_global_protect_regional_and_custom_proxies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionalAndCustomProxiesApi->create_global_protect_regional_and_custom_proxies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **forwarding_profile_regional_and_custom_proxies** | [**ForwardingProfileRegionalAndCustomProxies**](ForwardingProfileRegionalAndCustomProxies.md)| Created | [optional] 

### Return type

[**ForwardingProfileRegionalAndCustomProxies**](ForwardingProfileRegionalAndCustomProxies.md)

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

# **delete_global_protect_regional_and_custom_proxies**
> delete_global_protect_regional_and_custom_proxies(id)

Delete a GlobalProtect regional and custom proxy

Delete a GlobalProtect regional and custom proxy 

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
    api_instance = scm.mobile_agent.RegionalAndCustomProxiesApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Delete a GlobalProtect regional and custom proxy
        api_instance.delete_global_protect_regional_and_custom_proxies(id)
    except Exception as e:
        print("Exception when calling RegionalAndCustomProxiesApi->delete_global_protect_regional_and_custom_proxies: %s\n" % e)
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

# **get_global_protect_regional_and_custom_proxy_by_id**
> ForwardingProfileRegionalAndCustomProxies get_global_protect_regional_and_custom_proxy_by_id(id)

Get a GlobalProtect regional and custom proxy

Retrieve an existing GlobalProtect regional and custom proxy 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies import ForwardingProfileRegionalAndCustomProxies
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
    api_instance = scm.mobile_agent.RegionalAndCustomProxiesApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get a GlobalProtect regional and custom proxy
        api_response = api_instance.get_global_protect_regional_and_custom_proxy_by_id(id)
        print("The response of RegionalAndCustomProxiesApi->get_global_protect_regional_and_custom_proxy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionalAndCustomProxiesApi->get_global_protect_regional_and_custom_proxy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**ForwardingProfileRegionalAndCustomProxies**](ForwardingProfileRegionalAndCustomProxies.md)

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

# **list_global_protect_regional_and_custom_proxies**
> GlobalProtectRegionalAndCustomProxiesListResponse list_global_protect_regional_and_custom_proxies(name=name, limit=limit, offset=offset, folder=folder)

List GlobalProtect regional and custom proxies

Retrieve a list of GlobalProtect regional and custom proxies 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.global_protect_regional_and_custom_proxies_list_response import GlobalProtectRegionalAndCustomProxiesListResponse
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
    api_instance = scm.mobile_agent.RegionalAndCustomProxiesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)

    try:
        # List GlobalProtect regional and custom proxies
        api_response = api_instance.list_global_protect_regional_and_custom_proxies(name=name, limit=limit, offset=offset, folder=folder)
        print("The response of RegionalAndCustomProxiesApi->list_global_protect_regional_and_custom_proxies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionalAndCustomProxiesApi->list_global_protect_regional_and_custom_proxies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **folder** | **str**| The folder in which the resource is defined  | [optional] 

### Return type

[**GlobalProtectRegionalAndCustomProxiesListResponse**](GlobalProtectRegionalAndCustomProxiesListResponse.md)

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

# **update_global_protect_regional_and_custom_proxy_by_id**
> ForwardingProfileRegionalAndCustomProxies update_global_protect_regional_and_custom_proxy_by_id(id, forwarding_profile_regional_and_custom_proxies=forwarding_profile_regional_and_custom_proxies)

Update a GlobalProtect regional and custom proxy

Update an existing GlobalProtect regional and custom proxy 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies import ForwardingProfileRegionalAndCustomProxies
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
    api_instance = scm.mobile_agent.RegionalAndCustomProxiesApi(api_client)
    id = 'id_example' # str | The UUID of the resource
    forwarding_profile_regional_and_custom_proxies = scm.mobile_agent.ForwardingProfileRegionalAndCustomProxies() # ForwardingProfileRegionalAndCustomProxies | The regional and custom proxy resource definition (optional)

    try:
        # Update a GlobalProtect regional and custom proxy
        api_response = api_instance.update_global_protect_regional_and_custom_proxy_by_id(id, forwarding_profile_regional_and_custom_proxies=forwarding_profile_regional_and_custom_proxies)
        print("The response of RegionalAndCustomProxiesApi->update_global_protect_regional_and_custom_proxy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionalAndCustomProxiesApi->update_global_protect_regional_and_custom_proxy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 
 **forwarding_profile_regional_and_custom_proxies** | [**ForwardingProfileRegionalAndCustomProxies**](ForwardingProfileRegionalAndCustomProxies.md)| The regional and custom proxy resource definition | [optional] 

### Return type

[**ForwardingProfileRegionalAndCustomProxies**](ForwardingProfileRegionalAndCustomProxies.md)

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

