# scm_network_services.ZoneProtectionProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_zone_protection_profiles**](ZoneProtectionProfilesApi.md#create_zone_protection_profiles) | **POST** /zone-protection-profiles | Create a zone protection profile
[**delete_zone_protection_profiles_by_id**](ZoneProtectionProfilesApi.md#delete_zone_protection_profiles_by_id) | **DELETE** /zone-protection-profiles/{id} | Delete a zone protection profile
[**get_zone_protection_profiles_by_id**](ZoneProtectionProfilesApi.md#get_zone_protection_profiles_by_id) | **GET** /zone-protection-profiles/{id} | Get a zone protection profile
[**list_zone_protection_profiles**](ZoneProtectionProfilesApi.md#list_zone_protection_profiles) | **GET** /zone-protection-profiles | List zone protection profiles
[**update_zone_protection_profiles_by_id**](ZoneProtectionProfilesApi.md#update_zone_protection_profiles_by_id) | **PUT** /zone-protection-profiles/{id} | Update a zone protection profile


# **create_zone_protection_profiles**
> ZoneProtectionProfiles create_zone_protection_profiles(zone_protection_profiles=zone_protection_profiles)

Create a zone protection profile

Create a new zone protection profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.zone_protection_profiles import ZoneProtectionProfiles
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
    api_instance = scm_network_services.ZoneProtectionProfilesApi(api_client)
    zone_protection_profiles = scm_network_services.ZoneProtectionProfiles() # ZoneProtectionProfiles | Created (optional)

    try:
        # Create a zone protection profile
        api_response = api_instance.create_zone_protection_profiles(zone_protection_profiles=zone_protection_profiles)
        print("The response of ZoneProtectionProfilesApi->create_zone_protection_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneProtectionProfilesApi->create_zone_protection_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_protection_profiles** | [**ZoneProtectionProfiles**](ZoneProtectionProfiles.md)| Created | [optional] 

### Return type

[**ZoneProtectionProfiles**](ZoneProtectionProfiles.md)

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

# **delete_zone_protection_profiles_by_id**
> delete_zone_protection_profiles_by_id(id)

Delete a zone protection profile

Delete a zone protection profile. 

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
    api_instance = scm_network_services.ZoneProtectionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a zone protection profile
        api_instance.delete_zone_protection_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling ZoneProtectionProfilesApi->delete_zone_protection_profiles_by_id: %s\n" % e)
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

# **get_zone_protection_profiles_by_id**
> ZoneProtectionProfiles get_zone_protection_profiles_by_id(id)

Get a zone protection profile

Get an existing zone protection profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.zone_protection_profiles import ZoneProtectionProfiles
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
    api_instance = scm_network_services.ZoneProtectionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a zone protection profile
        api_response = api_instance.get_zone_protection_profiles_by_id(id)
        print("The response of ZoneProtectionProfilesApi->get_zone_protection_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneProtectionProfilesApi->get_zone_protection_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**ZoneProtectionProfiles**](ZoneProtectionProfiles.md)

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

# **list_zone_protection_profiles**
> ZoneProtectionProfilesListResponse list_zone_protection_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List zone protection profiles

Retrieve a list of zone protection profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.zone_protection_profiles_list_response import ZoneProtectionProfilesListResponse
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
    api_instance = scm_network_services.ZoneProtectionProfilesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List zone protection profiles
        api_response = api_instance.list_zone_protection_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of ZoneProtectionProfilesApi->list_zone_protection_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneProtectionProfilesApi->list_zone_protection_profiles: %s\n" % e)
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

[**ZoneProtectionProfilesListResponse**](ZoneProtectionProfilesListResponse.md)

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

# **update_zone_protection_profiles_by_id**
> ZoneProtectionProfiles update_zone_protection_profiles_by_id(id, zone_protection_profiles=zone_protection_profiles)

Update a zone protection profile

Update an existing zone protection profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.zone_protection_profiles import ZoneProtectionProfiles
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
    api_instance = scm_network_services.ZoneProtectionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    zone_protection_profiles = scm_network_services.ZoneProtectionProfiles() # ZoneProtectionProfiles | OK (optional)

    try:
        # Update a zone protection profile
        api_response = api_instance.update_zone_protection_profiles_by_id(id, zone_protection_profiles=zone_protection_profiles)
        print("The response of ZoneProtectionProfilesApi->update_zone_protection_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneProtectionProfilesApi->update_zone_protection_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **zone_protection_profiles** | [**ZoneProtectionProfiles**](ZoneProtectionProfiles.md)| OK | [optional] 

### Return type

[**ZoneProtectionProfiles**](ZoneProtectionProfiles.md)

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

