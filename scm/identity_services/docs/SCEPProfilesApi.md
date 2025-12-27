# scm_identity_services.SCEPProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scep_profiles**](SCEPProfilesApi.md#create_scep_profiles) | **POST** /scep-profiles | Create a SCEP profile
[**delete_scep_profiles_by_id**](SCEPProfilesApi.md#delete_scep_profiles_by_id) | **DELETE** /scep-profiles/{id} | Delete a SCEP profile
[**get_scep_profiles_by_id**](SCEPProfilesApi.md#get_scep_profiles_by_id) | **GET** /scep-profiles/{id} | Get a SCEP profile
[**list_scep_profiles**](SCEPProfilesApi.md#list_scep_profiles) | **GET** /scep-profiles | List SCEP profiles
[**update_scep_profiles_by_id**](SCEPProfilesApi.md#update_scep_profiles_by_id) | **PUT** /scep-profiles/{id} | Update a SCEP profile


# **create_scep_profiles**
> ScepProfiles create_scep_profiles(scep_profiles=scep_profiles)

Create a SCEP profile

Create a new SCEP profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.scep_profiles import ScepProfiles
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
    api_instance = scm_identity_services.SCEPProfilesApi(api_client)
    scep_profiles = scm_identity_services.ScepProfiles() # ScepProfiles | Created (optional)

    try:
        # Create a SCEP profile
        api_response = api_instance.create_scep_profiles(scep_profiles=scep_profiles)
        print("The response of SCEPProfilesApi->create_scep_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfilesApi->create_scep_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scep_profiles** | [**ScepProfiles**](ScepProfiles.md)| Created | [optional] 

### Return type

[**ScepProfiles**](ScepProfiles.md)

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

# **delete_scep_profiles_by_id**
> delete_scep_profiles_by_id(id)

Delete a SCEP profile

Delete a SCEP profile. 

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
    api_instance = scm_identity_services.SCEPProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a SCEP profile
        api_instance.delete_scep_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling SCEPProfilesApi->delete_scep_profiles_by_id: %s\n" % e)
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

# **get_scep_profiles_by_id**
> ScepProfiles get_scep_profiles_by_id(id)

Get a SCEP profile

Get an existing SCEP profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.scep_profiles import ScepProfiles
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
    api_instance = scm_identity_services.SCEPProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a SCEP profile
        api_response = api_instance.get_scep_profiles_by_id(id)
        print("The response of SCEPProfilesApi->get_scep_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfilesApi->get_scep_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**ScepProfiles**](ScepProfiles.md)

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

# **list_scep_profiles**
> SCEPProfilesListResponse list_scep_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List SCEP profiles

Retrieve a list of SCEP profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.scep_profiles_list_response import SCEPProfilesListResponse
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
    api_instance = scm_identity_services.SCEPProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List SCEP profiles
        api_response = api_instance.list_scep_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of SCEPProfilesApi->list_scep_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfilesApi->list_scep_profiles: %s\n" % e)
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

[**SCEPProfilesListResponse**](SCEPProfilesListResponse.md)

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

# **update_scep_profiles_by_id**
> ScepProfiles update_scep_profiles_by_id(id, scep_profiles=scep_profiles)

Update a SCEP profile

Update an existing SCEP profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.scep_profiles import ScepProfiles
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
    api_instance = scm_identity_services.SCEPProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    scep_profiles = scm_identity_services.ScepProfiles() # ScepProfiles | OK (optional)

    try:
        # Update a SCEP profile
        api_response = api_instance.update_scep_profiles_by_id(id, scep_profiles=scep_profiles)
        print("The response of SCEPProfilesApi->update_scep_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfilesApi->update_scep_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **scep_profiles** | [**ScepProfiles**](ScepProfiles.md)| OK | [optional] 

### Return type

[**ScepProfiles**](ScepProfiles.md)

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

