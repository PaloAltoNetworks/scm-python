# scm_objects.HIPProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hip_profiles**](HIPProfilesApi.md#create_hip_profiles) | **POST** /hip-profiles | Create a HIP profile
[**delete_hip_profiles_by_id**](HIPProfilesApi.md#delete_hip_profiles_by_id) | **DELETE** /hip-profiles/{id} | Delete a HIP profile
[**get_hip_profiles_by_id**](HIPProfilesApi.md#get_hip_profiles_by_id) | **GET** /hip-profiles/{id} | Get a HIP profile
[**list_hip_profiles**](HIPProfilesApi.md#list_hip_profiles) | **GET** /hip-profiles | List HIP profiles
[**update_hip_profiles_by_id**](HIPProfilesApi.md#update_hip_profiles_by_id) | **PUT** /hip-profiles/{id} | Update a HIP profile


# **create_hip_profiles**
> HipProfiles create_hip_profiles(hip_profiles=hip_profiles)

Create a HIP profile

Create a new HIP profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.hip_profiles import HipProfiles
from scm_objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_objects.HIPProfilesApi(api_client)
    hip_profiles = scm_objects.HipProfiles() # HipProfiles | Created (optional)

    try:
        # Create a HIP profile
        api_response = api_instance.create_hip_profiles(hip_profiles=hip_profiles)
        print("The response of HIPProfilesApi->create_hip_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HIPProfilesApi->create_hip_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hip_profiles** | [**HipProfiles**](HipProfiles.md)| Created | [optional] 

### Return type

[**HipProfiles**](HipProfiles.md)

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

# **delete_hip_profiles_by_id**
> delete_hip_profiles_by_id(id)

Delete a HIP profile

Delete a HIP profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_objects.HIPProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a HIP profile
        api_instance.delete_hip_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling HIPProfilesApi->delete_hip_profiles_by_id: %s\n" % e)
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

# **get_hip_profiles_by_id**
> HipProfiles get_hip_profiles_by_id(id)

Get a HIP profile

Get an existing HIP profile.

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.hip_profiles import HipProfiles
from scm_objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_objects.HIPProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a HIP profile
        api_response = api_instance.get_hip_profiles_by_id(id)
        print("The response of HIPProfilesApi->get_hip_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HIPProfilesApi->get_hip_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**HipProfiles**](HipProfiles.md)

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

# **list_hip_profiles**
> HIPProfilesListResponse list_hip_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List HIP profiles

Retrieve a list of HIP profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.hip_profiles_list_response import HIPProfilesListResponse
from scm_objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_objects.HIPProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List HIP profiles
        api_response = api_instance.list_hip_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of HIPProfilesApi->list_hip_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HIPProfilesApi->list_hip_profiles: %s\n" % e)
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

[**HIPProfilesListResponse**](HIPProfilesListResponse.md)

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

# **update_hip_profiles_by_id**
> HipProfiles update_hip_profiles_by_id(id, hip_profiles=hip_profiles)

Update a HIP profile

Update an existing HIP profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.hip_profiles import HipProfiles
from scm_objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_objects.HIPProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    hip_profiles = scm_objects.HipProfiles() # HipProfiles | OK (optional)

    try:
        # Update a HIP profile
        api_response = api_instance.update_hip_profiles_by_id(id, hip_profiles=hip_profiles)
        print("The response of HIPProfilesApi->update_hip_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HIPProfilesApi->update_hip_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **hip_profiles** | [**HipProfiles**](HipProfiles.md)| OK | [optional] 

### Return type

[**HipProfiles**](HipProfiles.md)

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

