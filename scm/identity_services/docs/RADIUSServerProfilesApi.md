# scm.identity_services.RADIUSServerProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_radius_server_profiles**](RADIUSServerProfilesApi.md#create_radius_server_profiles) | **POST** /radius-server-profiles | Create a RADIUS server profile
[**delete_radius_server_profiles_by_id**](RADIUSServerProfilesApi.md#delete_radius_server_profiles_by_id) | **DELETE** /radius-server-profiles/{id} | Delete a RADIUS server profile
[**get_radius_server_profiles_by_id**](RADIUSServerProfilesApi.md#get_radius_server_profiles_by_id) | **GET** /radius-server-profiles/{id} | Get a RADIUS server profile
[**list_radius_server_profiles**](RADIUSServerProfilesApi.md#list_radius_server_profiles) | **GET** /radius-server-profiles | List RADIUS server profiles
[**update_radius_server_profiles_by_id**](RADIUSServerProfilesApi.md#update_radius_server_profiles_by_id) | **PUT** /radius-server-profiles/{id} | Update a RADIUS server profile


# **create_radius_server_profiles**
> RadiusServerProfiles create_radius_server_profiles(radius_server_profiles=radius_server_profiles)

Create a RADIUS server profile

Create a new RADIUS server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.radius_server_profiles import RadiusServerProfiles
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.RADIUSServerProfilesApi(api_client)
    radius_server_profiles = scm.identity_services.RadiusServerProfiles() # RadiusServerProfiles | Created (optional)

    try:
        # Create a RADIUS server profile
        api_response = api_instance.create_radius_server_profiles(radius_server_profiles=radius_server_profiles)
        print("The response of RADIUSServerProfilesApi->create_radius_server_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RADIUSServerProfilesApi->create_radius_server_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius_server_profiles** | [**RadiusServerProfiles**](RadiusServerProfiles.md)| Created | [optional] 

### Return type

[**RadiusServerProfiles**](RadiusServerProfiles.md)

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

# **delete_radius_server_profiles_by_id**
> delete_radius_server_profiles_by_id(id)

Delete a RADIUS server profile

Delete a RADIUS server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.RADIUSServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a RADIUS server profile
        api_instance.delete_radius_server_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling RADIUSServerProfilesApi->delete_radius_server_profiles_by_id: %s\n" % e)
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

# **get_radius_server_profiles_by_id**
> RadiusServerProfiles get_radius_server_profiles_by_id(id)

Get a RADIUS server profile

Get an existing RADIUS server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.radius_server_profiles import RadiusServerProfiles
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.RADIUSServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a RADIUS server profile
        api_response = api_instance.get_radius_server_profiles_by_id(id)
        print("The response of RADIUSServerProfilesApi->get_radius_server_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RADIUSServerProfilesApi->get_radius_server_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**RadiusServerProfiles**](RadiusServerProfiles.md)

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

# **list_radius_server_profiles**
> RADIUSServerProfilesListResponse list_radius_server_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List RADIUS server profiles

Retreive a list of RADIUS server profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.radius_server_profiles_list_response import RADIUSServerProfilesListResponse
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.RADIUSServerProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List RADIUS server profiles
        api_response = api_instance.list_radius_server_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of RADIUSServerProfilesApi->list_radius_server_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RADIUSServerProfilesApi->list_radius_server_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]

### Return type

[**RADIUSServerProfilesListResponse**](RADIUSServerProfilesListResponse.md)

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

# **update_radius_server_profiles_by_id**
> RadiusServerProfiles update_radius_server_profiles_by_id(id, radius_server_profiles=radius_server_profiles)

Update a RADIUS server profile

Update an existing RADIUS server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.radius_server_profiles import RadiusServerProfiles
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.RADIUSServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    radius_server_profiles = scm.identity_services.RadiusServerProfiles() # RadiusServerProfiles | OK (optional)

    try:
        # Update a RADIUS server profile
        api_response = api_instance.update_radius_server_profiles_by_id(id, radius_server_profiles=radius_server_profiles)
        print("The response of RADIUSServerProfilesApi->update_radius_server_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RADIUSServerProfilesApi->update_radius_server_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **radius_server_profiles** | [**RadiusServerProfiles**](RadiusServerProfiles.md)| OK | [optional] 

### Return type

[**RadiusServerProfiles**](RadiusServerProfiles.md)

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

