# scm.security_services.HTTPHeaderProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_http_header_profiles**](HTTPHeaderProfilesApi.md#create_http_header_profiles) | **POST** /http-header-profiles | Create an HTTP header profile
[**delete_http_header_profiles_by_id**](HTTPHeaderProfilesApi.md#delete_http_header_profiles_by_id) | **DELETE** /http-header-profiles/{id} | Delete an HTTP header profile
[**get_http_header_profiles_by_id**](HTTPHeaderProfilesApi.md#get_http_header_profiles_by_id) | **GET** /http-header-profiles/{id} | Get an HTTP header profile
[**list_http_header_profiles**](HTTPHeaderProfilesApi.md#list_http_header_profiles) | **GET** /http-header-profiles | List HTTP header profiles
[**update_http_header_profiles_by_id**](HTTPHeaderProfilesApi.md#update_http_header_profiles_by_id) | **PUT** /http-header-profiles/{id} | Update an HTTP header profile


# **create_http_header_profiles**
> HttpHeaderProfiles create_http_header_profiles(http_header_profiles=http_header_profiles)

Create an HTTP header profile

Create a new HTTP header profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.http_header_profiles import HttpHeaderProfiles
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.HTTPHeaderProfilesApi(api_client)
    http_header_profiles = scm.security_services.HttpHeaderProfiles() # HttpHeaderProfiles | Created (optional)

    try:
        # Create an HTTP header profile
        api_response = api_instance.create_http_header_profiles(http_header_profiles=http_header_profiles)
        print("The response of HTTPHeaderProfilesApi->create_http_header_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPHeaderProfilesApi->create_http_header_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_header_profiles** | [**HttpHeaderProfiles**](HttpHeaderProfiles.md)| Created | [optional] 

### Return type

[**HttpHeaderProfiles**](HttpHeaderProfiles.md)

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

# **delete_http_header_profiles_by_id**
> delete_http_header_profiles_by_id(id)

Delete an HTTP header profile

Delete an HTTP header profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.HTTPHeaderProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an HTTP header profile
        api_instance.delete_http_header_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling HTTPHeaderProfilesApi->delete_http_header_profiles_by_id: %s\n" % e)
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

# **get_http_header_profiles_by_id**
> HttpHeaderProfiles get_http_header_profiles_by_id(id)

Get an HTTP header profile

Get an existing HTTP header profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.http_header_profiles import HttpHeaderProfiles
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.HTTPHeaderProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an HTTP header profile
        api_response = api_instance.get_http_header_profiles_by_id(id)
        print("The response of HTTPHeaderProfilesApi->get_http_header_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPHeaderProfilesApi->get_http_header_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**HttpHeaderProfiles**](HttpHeaderProfiles.md)

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

# **list_http_header_profiles**
> HTTPHeaderProfilesListResponse list_http_header_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List HTTP header profiles

Retrieve a list of HTTP header profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.http_header_profiles_list_response import HTTPHeaderProfilesListResponse
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.HTTPHeaderProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List HTTP header profiles
        api_response = api_instance.list_http_header_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of HTTPHeaderProfilesApi->list_http_header_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPHeaderProfilesApi->list_http_header_profiles: %s\n" % e)
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

[**HTTPHeaderProfilesListResponse**](HTTPHeaderProfilesListResponse.md)

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

# **update_http_header_profiles_by_id**
> HttpHeaderProfiles update_http_header_profiles_by_id(id, http_header_profiles=http_header_profiles)

Update an HTTP header profile

Update an existing HTTP header profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.http_header_profiles import HttpHeaderProfiles
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.HTTPHeaderProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    http_header_profiles = scm.security_services.HttpHeaderProfiles() # HttpHeaderProfiles | OK (optional)

    try:
        # Update an HTTP header profile
        api_response = api_instance.update_http_header_profiles_by_id(id, http_header_profiles=http_header_profiles)
        print("The response of HTTPHeaderProfilesApi->update_http_header_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPHeaderProfilesApi->update_http_header_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **http_header_profiles** | [**HttpHeaderProfiles**](HttpHeaderProfiles.md)| OK | [optional] 

### Return type

[**HttpHeaderProfiles**](HttpHeaderProfiles.md)

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

