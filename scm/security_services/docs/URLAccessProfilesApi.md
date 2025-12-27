# scm.security_services.URLAccessProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_url_access_profiles**](URLAccessProfilesApi.md#create_url_access_profiles) | **POST** /url-access-profiles | Create a URL access profile
[**delete_url_access_profiles_by_id**](URLAccessProfilesApi.md#delete_url_access_profiles_by_id) | **DELETE** /url-access-profiles/{id} | Delete a URL access profile
[**get_url_access_profiles_by_id**](URLAccessProfilesApi.md#get_url_access_profiles_by_id) | **GET** /url-access-profiles/{id} | Get a URL access profile
[**list_url_access_profiles**](URLAccessProfilesApi.md#list_url_access_profiles) | **GET** /url-access-profiles | List URL access profiles
[**update_url_access_profiles_by_id**](URLAccessProfilesApi.md#update_url_access_profiles_by_id) | **PUT** /url-access-profiles/{id} | Update a URL access Profile


# **create_url_access_profiles**
> UrlAccessProfiles create_url_access_profiles(url_access_profiles=url_access_profiles)

Create a URL access profile

Create a new URL access profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.url_access_profiles import UrlAccessProfiles
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
    api_instance = scm.security_services.URLAccessProfilesApi(api_client)
    url_access_profiles = scm.security_services.UrlAccessProfiles() # UrlAccessProfiles | Created (optional)

    try:
        # Create a URL access profile
        api_response = api_instance.create_url_access_profiles(url_access_profiles=url_access_profiles)
        print("The response of URLAccessProfilesApi->create_url_access_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling URLAccessProfilesApi->create_url_access_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_access_profiles** | [**UrlAccessProfiles**](UrlAccessProfiles.md)| Created | [optional] 

### Return type

[**UrlAccessProfiles**](UrlAccessProfiles.md)

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

# **delete_url_access_profiles_by_id**
> delete_url_access_profiles_by_id(id)

Delete a URL access profile

Delete a URL access profile. 

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
    api_instance = scm.security_services.URLAccessProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a URL access profile
        api_instance.delete_url_access_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling URLAccessProfilesApi->delete_url_access_profiles_by_id: %s\n" % e)
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

# **get_url_access_profiles_by_id**
> UrlAccessProfiles get_url_access_profiles_by_id(id)

Get a URL access profile

Get an existing URL access profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.url_access_profiles import UrlAccessProfiles
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
    api_instance = scm.security_services.URLAccessProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a URL access profile
        api_response = api_instance.get_url_access_profiles_by_id(id)
        print("The response of URLAccessProfilesApi->get_url_access_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling URLAccessProfilesApi->get_url_access_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**UrlAccessProfiles**](UrlAccessProfiles.md)

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

# **list_url_access_profiles**
> URLAccessProfilesListResponse list_url_access_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List URL access profiles

Retrieve a list of URL access profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.url_access_profiles_list_response import URLAccessProfilesListResponse
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
    api_instance = scm.security_services.URLAccessProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List URL access profiles
        api_response = api_instance.list_url_access_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of URLAccessProfilesApi->list_url_access_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling URLAccessProfilesApi->list_url_access_profiles: %s\n" % e)
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

[**URLAccessProfilesListResponse**](URLAccessProfilesListResponse.md)

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

# **update_url_access_profiles_by_id**
> UrlAccessProfiles update_url_access_profiles_by_id(id, url_access_profiles=url_access_profiles)

Update a URL access Profile

Update an existing URL access Profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.url_access_profiles import UrlAccessProfiles
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
    api_instance = scm.security_services.URLAccessProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    url_access_profiles = scm.security_services.UrlAccessProfiles() # UrlAccessProfiles | OK (optional)

    try:
        # Update a URL access Profile
        api_response = api_instance.update_url_access_profiles_by_id(id, url_access_profiles=url_access_profiles)
        print("The response of URLAccessProfilesApi->update_url_access_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling URLAccessProfilesApi->update_url_access_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **url_access_profiles** | [**UrlAccessProfiles**](UrlAccessProfiles.md)| OK | [optional] 

### Return type

[**UrlAccessProfiles**](UrlAccessProfiles.md)

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

