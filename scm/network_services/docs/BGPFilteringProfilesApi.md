# scm.network_services.BGPFilteringProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bgp_filtering_profiles**](BGPFilteringProfilesApi.md#create_bgp_filtering_profiles) | **POST** /bgp-filtering-profiles | Create a BGP filtering profile
[**delete_bgp_filtering_profiles_by_id**](BGPFilteringProfilesApi.md#delete_bgp_filtering_profiles_by_id) | **DELETE** /bgp-filtering-profiles/{id} | Delete a BGP filtering profile
[**get_bgp_filtering_profiles_by_id**](BGPFilteringProfilesApi.md#get_bgp_filtering_profiles_by_id) | **GET** /bgp-filtering-profiles/{id} | Get a BGP filtering profile
[**list_bgp_filtering_profiles**](BGPFilteringProfilesApi.md#list_bgp_filtering_profiles) | **GET** /bgp-filtering-profiles | List BGP filtering profiles
[**update_bgp_filtering_profiles_by_id**](BGPFilteringProfilesApi.md#update_bgp_filtering_profiles_by_id) | **PUT** /bgp-filtering-profiles/{id} | Update a BGP filtering profile


# **create_bgp_filtering_profiles**
> BgpFilteringProfiles create_bgp_filtering_profiles(bgp_filtering_profiles=bgp_filtering_profiles)

Create a BGP filtering profile

Create a new BGP filtering profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.bgp_filtering_profiles import BgpFilteringProfiles
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
    api_instance = scm.network_services.BGPFilteringProfilesApi(api_client)
    bgp_filtering_profiles = scm.network_services.BgpFilteringProfiles() # BgpFilteringProfiles | Created (optional)

    try:
        # Create a BGP filtering profile
        api_response = api_instance.create_bgp_filtering_profiles(bgp_filtering_profiles=bgp_filtering_profiles)
        print("The response of BGPFilteringProfilesApi->create_bgp_filtering_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPFilteringProfilesApi->create_bgp_filtering_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_filtering_profiles** | [**BgpFilteringProfiles**](BgpFilteringProfiles.md)| Created | [optional] 

### Return type

[**BgpFilteringProfiles**](BgpFilteringProfiles.md)

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

# **delete_bgp_filtering_profiles_by_id**
> delete_bgp_filtering_profiles_by_id(id)

Delete a BGP filtering profile

Delete a BGP filtering profile. 

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
    api_instance = scm.network_services.BGPFilteringProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a BGP filtering profile
        api_instance.delete_bgp_filtering_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling BGPFilteringProfilesApi->delete_bgp_filtering_profiles_by_id: %s\n" % e)
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

# **get_bgp_filtering_profiles_by_id**
> BgpFilteringProfiles get_bgp_filtering_profiles_by_id(id)

Get a BGP filtering profile

Get an existing BGP filtering profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.bgp_filtering_profiles import BgpFilteringProfiles
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
    api_instance = scm.network_services.BGPFilteringProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a BGP filtering profile
        api_response = api_instance.get_bgp_filtering_profiles_by_id(id)
        print("The response of BGPFilteringProfilesApi->get_bgp_filtering_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPFilteringProfilesApi->get_bgp_filtering_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**BgpFilteringProfiles**](BgpFilteringProfiles.md)

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

# **list_bgp_filtering_profiles**
> BGPFilteringProfilesListResponse list_bgp_filtering_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List BGP filtering profiles

Retrieve a list of BGP filtering profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.bgp_filtering_profiles_list_response import BGPFilteringProfilesListResponse
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
    api_instance = scm.network_services.BGPFilteringProfilesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List BGP filtering profiles
        api_response = api_instance.list_bgp_filtering_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of BGPFilteringProfilesApi->list_bgp_filtering_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPFilteringProfilesApi->list_bgp_filtering_profiles: %s\n" % e)
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

[**BGPFilteringProfilesListResponse**](BGPFilteringProfilesListResponse.md)

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

# **update_bgp_filtering_profiles_by_id**
> BgpFilteringProfiles update_bgp_filtering_profiles_by_id(id, bgp_filtering_profiles=bgp_filtering_profiles)

Update a BGP filtering profile

Update an existing BGP filtering profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.bgp_filtering_profiles import BgpFilteringProfiles
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
    api_instance = scm.network_services.BGPFilteringProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    bgp_filtering_profiles = scm.network_services.BgpFilteringProfiles() # BgpFilteringProfiles | OK (optional)

    try:
        # Update a BGP filtering profile
        api_response = api_instance.update_bgp_filtering_profiles_by_id(id, bgp_filtering_profiles=bgp_filtering_profiles)
        print("The response of BGPFilteringProfilesApi->update_bgp_filtering_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPFilteringProfilesApi->update_bgp_filtering_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **bgp_filtering_profiles** | [**BgpFilteringProfiles**](BgpFilteringProfiles.md)| OK | [optional] 

### Return type

[**BgpFilteringProfiles**](BgpFilteringProfiles.md)

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

