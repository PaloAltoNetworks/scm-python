# scm_network_services.SDWANErrorCorrectionProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sdwan_error_correction_profiles**](SDWANErrorCorrectionProfilesApi.md#create_sdwan_error_correction_profiles) | **POST** /sdwan-error-correction-profiles | Create an SD-WAN error correction profile
[**delete_sdwan_error_correction_profiles_by_id**](SDWANErrorCorrectionProfilesApi.md#delete_sdwan_error_correction_profiles_by_id) | **DELETE** /sdwan-error-correction-profiles/{id} | Delete an SD-WAN error correction profile
[**get_sdwan_error_correction_profiles_by_id**](SDWANErrorCorrectionProfilesApi.md#get_sdwan_error_correction_profiles_by_id) | **GET** /sdwan-error-correction-profiles/{id} | Get an SD-WAN error correction profile
[**list_sdwan_error_correction_profiles**](SDWANErrorCorrectionProfilesApi.md#list_sdwan_error_correction_profiles) | **GET** /sdwan-error-correction-profiles | List SD-WAN error correction profiles
[**update_sdwan_error_correction_profiles_by_id**](SDWANErrorCorrectionProfilesApi.md#update_sdwan_error_correction_profiles_by_id) | **PUT** /sdwan-error-correction-profiles/{id} | Update an SD-WAN error correction profile


# **create_sdwan_error_correction_profiles**
> SdwanErrorCorrectionProfiles create_sdwan_error_correction_profiles(sdwan_error_correction_profiles=sdwan_error_correction_profiles)

Create an SD-WAN error correction profile

Create a new SD-WAN error correction profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.sdwan_error_correction_profiles import SdwanErrorCorrectionProfiles
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.SDWANErrorCorrectionProfilesApi(api_client)
    sdwan_error_correction_profiles = scm_network_services.SdwanErrorCorrectionProfiles() # SdwanErrorCorrectionProfiles | Created (optional)

    try:
        # Create an SD-WAN error correction profile
        api_response = api_instance.create_sdwan_error_correction_profiles(sdwan_error_correction_profiles=sdwan_error_correction_profiles)
        print("The response of SDWANErrorCorrectionProfilesApi->create_sdwan_error_correction_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANErrorCorrectionProfilesApi->create_sdwan_error_correction_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdwan_error_correction_profiles** | [**SdwanErrorCorrectionProfiles**](SdwanErrorCorrectionProfiles.md)| Created | [optional] 

### Return type

[**SdwanErrorCorrectionProfiles**](SdwanErrorCorrectionProfiles.md)

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

# **delete_sdwan_error_correction_profiles_by_id**
> delete_sdwan_error_correction_profiles_by_id(id)

Delete an SD-WAN error correction profile

Delete an SD-WAN error correction profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.SDWANErrorCorrectionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an SD-WAN error correction profile
        api_instance.delete_sdwan_error_correction_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling SDWANErrorCorrectionProfilesApi->delete_sdwan_error_correction_profiles_by_id: %s\n" % e)
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

# **get_sdwan_error_correction_profiles_by_id**
> SdwanErrorCorrectionProfiles get_sdwan_error_correction_profiles_by_id(id)

Get an SD-WAN error correction profile

Get an existing SD-WAN error correction profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.sdwan_error_correction_profiles import SdwanErrorCorrectionProfiles
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.SDWANErrorCorrectionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an SD-WAN error correction profile
        api_response = api_instance.get_sdwan_error_correction_profiles_by_id(id)
        print("The response of SDWANErrorCorrectionProfilesApi->get_sdwan_error_correction_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANErrorCorrectionProfilesApi->get_sdwan_error_correction_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**SdwanErrorCorrectionProfiles**](SdwanErrorCorrectionProfiles.md)

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

# **list_sdwan_error_correction_profiles**
> SDWANErrorCorrectionProfilesListResponse list_sdwan_error_correction_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List SD-WAN error correction profiles

Retrieve a list of SD-WAN error correction profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.sdwan_error_correction_profiles_list_response import SDWANErrorCorrectionProfilesListResponse
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.SDWANErrorCorrectionProfilesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List SD-WAN error correction profiles
        api_response = api_instance.list_sdwan_error_correction_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of SDWANErrorCorrectionProfilesApi->list_sdwan_error_correction_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANErrorCorrectionProfilesApi->list_sdwan_error_correction_profiles: %s\n" % e)
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

[**SDWANErrorCorrectionProfilesListResponse**](SDWANErrorCorrectionProfilesListResponse.md)

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

# **update_sdwan_error_correction_profiles_by_id**
> SdwanErrorCorrectionProfiles update_sdwan_error_correction_profiles_by_id(id, sdwan_error_correction_profiles=sdwan_error_correction_profiles)

Update an SD-WAN error correction profile

Update an existing SD-WAN error correction profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.sdwan_error_correction_profiles import SdwanErrorCorrectionProfiles
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.SDWANErrorCorrectionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    sdwan_error_correction_profiles = scm_network_services.SdwanErrorCorrectionProfiles() # SdwanErrorCorrectionProfiles | OK (optional)

    try:
        # Update an SD-WAN error correction profile
        api_response = api_instance.update_sdwan_error_correction_profiles_by_id(id, sdwan_error_correction_profiles=sdwan_error_correction_profiles)
        print("The response of SDWANErrorCorrectionProfilesApi->update_sdwan_error_correction_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANErrorCorrectionProfilesApi->update_sdwan_error_correction_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **sdwan_error_correction_profiles** | [**SdwanErrorCorrectionProfiles**](SdwanErrorCorrectionProfiles.md)| OK | [optional] 

### Return type

[**SdwanErrorCorrectionProfiles**](SdwanErrorCorrectionProfiles.md)

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

