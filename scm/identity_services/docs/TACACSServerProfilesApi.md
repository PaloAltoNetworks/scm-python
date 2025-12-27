# scm_identity_services.TACACSServerProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tacacs_server_profiles**](TACACSServerProfilesApi.md#create_tacacs_server_profiles) | **POST** /tacacs-server-profiles | Create a TACACS server profile
[**delete_tacacs_server_profiles_by_id**](TACACSServerProfilesApi.md#delete_tacacs_server_profiles_by_id) | **DELETE** /tacacs-server-profiles/{id} | Delete a TACACS server profile
[**get_tacacs_server_profiles_by_id**](TACACSServerProfilesApi.md#get_tacacs_server_profiles_by_id) | **GET** /tacacs-server-profiles/{id} | Get a TACACS server profile
[**list_tacacs_server_profiles**](TACACSServerProfilesApi.md#list_tacacs_server_profiles) | **GET** /tacacs-server-profiles | List TACACS server profiles
[**update_tacacs_server_profiles_by_id**](TACACSServerProfilesApi.md#update_tacacs_server_profiles_by_id) | **PUT** /tacacs-server-profiles/{id} | Update a TACACS server profile


# **create_tacacs_server_profiles**
> TacacsServerProfiles create_tacacs_server_profiles(tacacs_server_profiles=tacacs_server_profiles)

Create a TACACS server profile

Create a new TACACS server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.tacacs_server_profiles import TacacsServerProfiles
from scm_identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_identity_services.TACACSServerProfilesApi(api_client)
    tacacs_server_profiles = scm_identity_services.TacacsServerProfiles() # TacacsServerProfiles | Created (optional)

    try:
        # Create a TACACS server profile
        api_response = api_instance.create_tacacs_server_profiles(tacacs_server_profiles=tacacs_server_profiles)
        print("The response of TACACSServerProfilesApi->create_tacacs_server_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TACACSServerProfilesApi->create_tacacs_server_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tacacs_server_profiles** | [**TacacsServerProfiles**](TacacsServerProfiles.md)| Created | [optional] 

### Return type

[**TacacsServerProfiles**](TacacsServerProfiles.md)

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
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tacacs_server_profiles_by_id**
> delete_tacacs_server_profiles_by_id(id)

Delete a TACACS server profile

Delete a TACACS server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_identity_services.TACACSServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a TACACS server profile
        api_instance.delete_tacacs_server_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling TACACSServerProfilesApi->delete_tacacs_server_profiles_by_id: %s\n" % e)
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

# **get_tacacs_server_profiles_by_id**
> TacacsServerProfiles get_tacacs_server_profiles_by_id(id)

Get a TACACS server profile

Get an existing TACACS server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.tacacs_server_profiles import TacacsServerProfiles
from scm_identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_identity_services.TACACSServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a TACACS server profile
        api_response = api_instance.get_tacacs_server_profiles_by_id(id)
        print("The response of TACACSServerProfilesApi->get_tacacs_server_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TACACSServerProfilesApi->get_tacacs_server_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**TacacsServerProfiles**](TacacsServerProfiles.md)

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

# **list_tacacs_server_profiles**
> TACACSServerProfilesListResponse list_tacacs_server_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List TACACS server profiles

Retrieve a list of TACACS server profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.tacacs_server_profiles_list_response import TACACSServerProfilesListResponse
from scm_identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_identity_services.TACACSServerProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List TACACS server profiles
        api_response = api_instance.list_tacacs_server_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of TACACSServerProfilesApi->list_tacacs_server_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TACACSServerProfilesApi->list_tacacs_server_profiles: %s\n" % e)
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

[**TACACSServerProfilesListResponse**](TACACSServerProfilesListResponse.md)

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

# **update_tacacs_server_profiles_by_id**
> TacacsServerProfiles update_tacacs_server_profiles_by_id(id, tacacs_server_profiles=tacacs_server_profiles)

Update a TACACS server profile

Update an existing TACACS server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.tacacs_server_profiles import TacacsServerProfiles
from scm_identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_identity_services.TACACSServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    tacacs_server_profiles = scm_identity_services.TacacsServerProfiles() # TacacsServerProfiles | OK (optional)

    try:
        # Update a TACACS server profile
        api_response = api_instance.update_tacacs_server_profiles_by_id(id, tacacs_server_profiles=tacacs_server_profiles)
        print("The response of TACACSServerProfilesApi->update_tacacs_server_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TACACSServerProfilesApi->update_tacacs_server_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **tacacs_server_profiles** | [**TacacsServerProfiles**](TacacsServerProfiles.md)| OK | [optional] 

### Return type

[**TacacsServerProfiles**](TacacsServerProfiles.md)

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

