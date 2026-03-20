# scm.objects.HTTPServerProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_http_server_profiles**](HTTPServerProfilesApi.md#create_http_server_profiles) | **POST** /http-server-profiles | Create a HTTP server profile
[**delete_http_server_profiles_by_id**](HTTPServerProfilesApi.md#delete_http_server_profiles_by_id) | **DELETE** /http-server-profiles/{id} | Delete a HTTP server profile
[**get_http_server_profiles_by_id**](HTTPServerProfilesApi.md#get_http_server_profiles_by_id) | **GET** /http-server-profiles/{id} | Get a HTTP server profile
[**list_http_server_profiles**](HTTPServerProfilesApi.md#list_http_server_profiles) | **GET** /http-server-profiles | List HTTP server profiles
[**update_http_server_profiles_by_id**](HTTPServerProfilesApi.md#update_http_server_profiles_by_id) | **PUT** /http-server-profiles/{id} | Update a HTTP server profile


# **create_http_server_profiles**
> HttpServerProfiles create_http_server_profiles(http_server_profiles=http_server_profiles)

Create a HTTP server profile

Create a new HTTP server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.http_server_profiles import HttpServerProfiles
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
    api_instance = scm.objects.HTTPServerProfilesApi(api_client)
    http_server_profiles = scm.objects.HttpServerProfiles() # HttpServerProfiles | Created (optional)

    try:
        # Create a HTTP server profile
        api_response = api_instance.create_http_server_profiles(http_server_profiles=http_server_profiles)
        print("The response of HTTPServerProfilesApi->create_http_server_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerProfilesApi->create_http_server_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_server_profiles** | [**HttpServerProfiles**](HttpServerProfiles.md)| Created | [optional] 

### Return type

[**HttpServerProfiles**](HttpServerProfiles.md)

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

# **delete_http_server_profiles_by_id**
> delete_http_server_profiles_by_id(id)

Delete a HTTP server profile

Delete a HTTP server profile. 

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
    api_instance = scm.objects.HTTPServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a HTTP server profile
        api_instance.delete_http_server_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling HTTPServerProfilesApi->delete_http_server_profiles_by_id: %s\n" % e)
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

# **get_http_server_profiles_by_id**
> HttpServerProfiles get_http_server_profiles_by_id(id)

Get a HTTP server profile

Get an existing HTTP server profile.

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.http_server_profiles import HttpServerProfiles
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
    api_instance = scm.objects.HTTPServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a HTTP server profile
        api_response = api_instance.get_http_server_profiles_by_id(id)
        print("The response of HTTPServerProfilesApi->get_http_server_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerProfilesApi->get_http_server_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**HttpServerProfiles**](HttpServerProfiles.md)

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

# **list_http_server_profiles**
> HTTPServerProfilesListResponse list_http_server_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List HTTP server profiles

Retrieve a list of HTTP server profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.http_server_profiles_list_response import HTTPServerProfilesListResponse
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
    api_instance = scm.objects.HTTPServerProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List HTTP server profiles
        api_response = api_instance.list_http_server_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of HTTPServerProfilesApi->list_http_server_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerProfilesApi->list_http_server_profiles: %s\n" % e)
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

[**HTTPServerProfilesListResponse**](HTTPServerProfilesListResponse.md)

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

# **update_http_server_profiles_by_id**
> HttpServerProfiles update_http_server_profiles_by_id(id, http_server_profiles=http_server_profiles)

Update a HTTP server profile

Update an existing HTTP server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.http_server_profiles import HttpServerProfiles
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
    api_instance = scm.objects.HTTPServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    http_server_profiles = scm.objects.HttpServerProfiles() # HttpServerProfiles | OK (optional)

    try:
        # Update a HTTP server profile
        api_response = api_instance.update_http_server_profiles_by_id(id, http_server_profiles=http_server_profiles)
        print("The response of HTTPServerProfilesApi->update_http_server_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerProfilesApi->update_http_server_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **http_server_profiles** | [**HttpServerProfiles**](HttpServerProfiles.md)| OK | [optional] 

### Return type

[**HttpServerProfiles**](HttpServerProfiles.md)

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

