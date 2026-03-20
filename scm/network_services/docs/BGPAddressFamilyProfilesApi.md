# scm.network_services.BGPAddressFamilyProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bgp_address_family_profiles**](BGPAddressFamilyProfilesApi.md#create_bgp_address_family_profiles) | **POST** /bgp-address-family-profiles | Create a BGP address family profile
[**delete_bgp_address_family_profiles_by_id**](BGPAddressFamilyProfilesApi.md#delete_bgp_address_family_profiles_by_id) | **DELETE** /bgp-address-family-profiles/{id} | Delete a BGP address family profile
[**get_bgp_address_family_profiles_by_id**](BGPAddressFamilyProfilesApi.md#get_bgp_address_family_profiles_by_id) | **GET** /bgp-address-family-profiles/{id} | Get a BGP address family profile
[**list_bgp_address_family_profiles**](BGPAddressFamilyProfilesApi.md#list_bgp_address_family_profiles) | **GET** /bgp-address-family-profiles | List BGP address family profiles
[**update_bgp_address_family_profiles_by_id**](BGPAddressFamilyProfilesApi.md#update_bgp_address_family_profiles_by_id) | **PUT** /bgp-address-family-profiles/{id} | Update a BGP address family profile


# **create_bgp_address_family_profiles**
> BgpAddressFamilyProfiles create_bgp_address_family_profiles(bgp_address_family_profiles=bgp_address_family_profiles)

Create a BGP address family profile

Create a new BGP address family profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.bgp_address_family_profiles import BgpAddressFamilyProfiles
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
    api_instance = scm.network_services.BGPAddressFamilyProfilesApi(api_client)
    bgp_address_family_profiles = scm.network_services.BgpAddressFamilyProfiles() # BgpAddressFamilyProfiles | Created (optional)

    try:
        # Create a BGP address family profile
        api_response = api_instance.create_bgp_address_family_profiles(bgp_address_family_profiles=bgp_address_family_profiles)
        print("The response of BGPAddressFamilyProfilesApi->create_bgp_address_family_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPAddressFamilyProfilesApi->create_bgp_address_family_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_address_family_profiles** | [**BgpAddressFamilyProfiles**](BgpAddressFamilyProfiles.md)| Created | [optional] 

### Return type

[**BgpAddressFamilyProfiles**](BgpAddressFamilyProfiles.md)

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

# **delete_bgp_address_family_profiles_by_id**
> delete_bgp_address_family_profiles_by_id(id)

Delete a BGP address family profile

Delete a BGP address family profile. 

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
    api_instance = scm.network_services.BGPAddressFamilyProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a BGP address family profile
        api_instance.delete_bgp_address_family_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling BGPAddressFamilyProfilesApi->delete_bgp_address_family_profiles_by_id: %s\n" % e)
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

# **get_bgp_address_family_profiles_by_id**
> BgpAddressFamilyProfiles get_bgp_address_family_profiles_by_id(id)

Get a BGP address family profile

Get an existing BGP address family profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.bgp_address_family_profiles import BgpAddressFamilyProfiles
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
    api_instance = scm.network_services.BGPAddressFamilyProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a BGP address family profile
        api_response = api_instance.get_bgp_address_family_profiles_by_id(id)
        print("The response of BGPAddressFamilyProfilesApi->get_bgp_address_family_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPAddressFamilyProfilesApi->get_bgp_address_family_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**BgpAddressFamilyProfiles**](BgpAddressFamilyProfiles.md)

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

# **list_bgp_address_family_profiles**
> BGPAddressFamilyProfilesListResponse list_bgp_address_family_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List BGP address family profiles

Retrieve a list of BGP address family profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.bgp_address_family_profiles_list_response import BGPAddressFamilyProfilesListResponse
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
    api_instance = scm.network_services.BGPAddressFamilyProfilesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List BGP address family profiles
        api_response = api_instance.list_bgp_address_family_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of BGPAddressFamilyProfilesApi->list_bgp_address_family_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPAddressFamilyProfilesApi->list_bgp_address_family_profiles: %s\n" % e)
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

[**BGPAddressFamilyProfilesListResponse**](BGPAddressFamilyProfilesListResponse.md)

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

# **update_bgp_address_family_profiles_by_id**
> BgpAddressFamilyProfiles update_bgp_address_family_profiles_by_id(id, bgp_address_family_profiles=bgp_address_family_profiles)

Update a BGP address family profile

Update an existing BGP address family profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.bgp_address_family_profiles import BgpAddressFamilyProfiles
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
    api_instance = scm.network_services.BGPAddressFamilyProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    bgp_address_family_profiles = scm.network_services.BgpAddressFamilyProfiles() # BgpAddressFamilyProfiles | OK (optional)

    try:
        # Update a BGP address family profile
        api_response = api_instance.update_bgp_address_family_profiles_by_id(id, bgp_address_family_profiles=bgp_address_family_profiles)
        print("The response of BGPAddressFamilyProfilesApi->update_bgp_address_family_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPAddressFamilyProfilesApi->update_bgp_address_family_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **bgp_address_family_profiles** | [**BgpAddressFamilyProfiles**](BgpAddressFamilyProfiles.md)| OK | [optional] 

### Return type

[**BgpAddressFamilyProfiles**](BgpAddressFamilyProfiles.md)

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

