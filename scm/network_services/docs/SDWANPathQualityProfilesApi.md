# scm.network_services.SDWANPathQualityProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sdwan_path_quality_profiles**](SDWANPathQualityProfilesApi.md#create_sdwan_path_quality_profiles) | **POST** /sdwan-path-quality-profiles | Create an SD-WAN path quality profile
[**delete_sdwan_path_quality_profiles_by_id**](SDWANPathQualityProfilesApi.md#delete_sdwan_path_quality_profiles_by_id) | **DELETE** /sdwan-path-quality-profiles/{id} | Delete an SD-WAN path quality profile
[**get_sdwan_path_quality_profiles_by_id**](SDWANPathQualityProfilesApi.md#get_sdwan_path_quality_profiles_by_id) | **GET** /sdwan-path-quality-profiles/{id} | Get an SD-WAN path quality profile
[**list_sdwan_path_quality_profiles**](SDWANPathQualityProfilesApi.md#list_sdwan_path_quality_profiles) | **GET** /sdwan-path-quality-profiles | List SD-WAN path quality profiles
[**update_sdwan_path_quality_profiles_by_id**](SDWANPathQualityProfilesApi.md#update_sdwan_path_quality_profiles_by_id) | **PUT** /sdwan-path-quality-profiles/{id} | Update an SD-WAN path quality profile


# **create_sdwan_path_quality_profiles**
> SdwanPathQualityProfiles create_sdwan_path_quality_profiles(sdwan_path_quality_profiles=sdwan_path_quality_profiles)

Create an SD-WAN path quality profile

Create a new SD-WAN path quality profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.sdwan_path_quality_profiles import SdwanPathQualityProfiles
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.SDWANPathQualityProfilesApi(api_client)
    sdwan_path_quality_profiles = scm.network_services.SdwanPathQualityProfiles() # SdwanPathQualityProfiles | Created (optional)

    try:
        # Create an SD-WAN path quality profile
        api_response = api_instance.create_sdwan_path_quality_profiles(sdwan_path_quality_profiles=sdwan_path_quality_profiles)
        print("The response of SDWANPathQualityProfilesApi->create_sdwan_path_quality_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANPathQualityProfilesApi->create_sdwan_path_quality_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdwan_path_quality_profiles** | [**SdwanPathQualityProfiles**](SdwanPathQualityProfiles.md)| Created | [optional] 

### Return type

[**SdwanPathQualityProfiles**](SdwanPathQualityProfiles.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sdwan_path_quality_profiles_by_id**
> delete_sdwan_path_quality_profiles_by_id(id)

Delete an SD-WAN path quality profile

Delete an SD-WAN path quality profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.SDWANPathQualityProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an SD-WAN path quality profile
        api_instance.delete_sdwan_path_quality_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling SDWANPathQualityProfilesApi->delete_sdwan_path_quality_profiles_by_id: %s\n" % e)
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
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdwan_path_quality_profiles_by_id**
> SdwanPathQualityProfiles get_sdwan_path_quality_profiles_by_id(id)

Get an SD-WAN path quality profile

Get an existing SD-WAN path quality profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.sdwan_path_quality_profiles import SdwanPathQualityProfiles
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.SDWANPathQualityProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an SD-WAN path quality profile
        api_response = api_instance.get_sdwan_path_quality_profiles_by_id(id)
        print("The response of SDWANPathQualityProfilesApi->get_sdwan_path_quality_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANPathQualityProfilesApi->get_sdwan_path_quality_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**SdwanPathQualityProfiles**](SdwanPathQualityProfiles.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sdwan_path_quality_profiles**
> SDWANPathQualityProfilesListResponse list_sdwan_path_quality_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List SD-WAN path quality profiles

Retrieve a list of SD-WAN path quality profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.sdwan_path_quality_profiles_list_response import SDWANPathQualityProfilesListResponse
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.SDWANPathQualityProfilesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List SD-WAN path quality profiles
        api_response = api_instance.list_sdwan_path_quality_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of SDWANPathQualityProfilesApi->list_sdwan_path_quality_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANPathQualityProfilesApi->list_sdwan_path_quality_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**SDWANPathQualityProfilesListResponse**](SDWANPathQualityProfilesListResponse.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sdwan_path_quality_profiles_by_id**
> SdwanPathQualityProfiles update_sdwan_path_quality_profiles_by_id(id, sdwan_path_quality_profiles=sdwan_path_quality_profiles)

Update an SD-WAN path quality profile

Update an existing SD-WAN path quality profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.sdwan_path_quality_profiles import SdwanPathQualityProfiles
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.SDWANPathQualityProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    sdwan_path_quality_profiles = scm.network_services.SdwanPathQualityProfiles() # SdwanPathQualityProfiles | OK (optional)

    try:
        # Update an SD-WAN path quality profile
        api_response = api_instance.update_sdwan_path_quality_profiles_by_id(id, sdwan_path_quality_profiles=sdwan_path_quality_profiles)
        print("The response of SDWANPathQualityProfilesApi->update_sdwan_path_quality_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANPathQualityProfilesApi->update_sdwan_path_quality_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **sdwan_path_quality_profiles** | [**SdwanPathQualityProfiles**](SdwanPathQualityProfiles.md)| OK | [optional] 

### Return type

[**SdwanPathQualityProfiles**](SdwanPathQualityProfiles.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

