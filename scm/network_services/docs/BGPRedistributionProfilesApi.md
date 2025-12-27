# scm_network_services.BGPRedistributionProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bgp_redistribution_profiles**](BGPRedistributionProfilesApi.md#create_bgp_redistribution_profiles) | **POST** /bgp-redistribution-profiles | Create a BGP redistribution profile
[**delete_bgp_redistribution_profiles_by_id**](BGPRedistributionProfilesApi.md#delete_bgp_redistribution_profiles_by_id) | **DELETE** /bgp-redistribution-profiles/{id} | Delete a BGP redistribution profile
[**get_bgp_redistribution_profiles_by_id**](BGPRedistributionProfilesApi.md#get_bgp_redistribution_profiles_by_id) | **GET** /bgp-redistribution-profiles/{id} | Get a BGP redistribution profile
[**list_bgp_redistribution_profiles**](BGPRedistributionProfilesApi.md#list_bgp_redistribution_profiles) | **GET** /bgp-redistribution-profiles | List BGP redistribution profiles
[**update_bgp_redistribution_profiles_by_id**](BGPRedistributionProfilesApi.md#update_bgp_redistribution_profiles_by_id) | **PUT** /bgp-redistribution-profiles/{id} | Update a BGP redistribution profile


# **create_bgp_redistribution_profiles**
> BgpRedistributionProfiles create_bgp_redistribution_profiles(bgp_redistribution_profiles=bgp_redistribution_profiles)

Create a BGP redistribution profile

Create a new BGP redistribution profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.bgp_redistribution_profiles import BgpRedistributionProfiles
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
    api_instance = scm_network_services.BGPRedistributionProfilesApi(api_client)
    bgp_redistribution_profiles = scm_network_services.BgpRedistributionProfiles() # BgpRedistributionProfiles | Created (optional)

    try:
        # Create a BGP redistribution profile
        api_response = api_instance.create_bgp_redistribution_profiles(bgp_redistribution_profiles=bgp_redistribution_profiles)
        print("The response of BGPRedistributionProfilesApi->create_bgp_redistribution_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPRedistributionProfilesApi->create_bgp_redistribution_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_redistribution_profiles** | [**BgpRedistributionProfiles**](BgpRedistributionProfiles.md)| Created | [optional] 

### Return type

[**BgpRedistributionProfiles**](BgpRedistributionProfiles.md)

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

# **delete_bgp_redistribution_profiles_by_id**
> delete_bgp_redistribution_profiles_by_id(id)

Delete a BGP redistribution profile

Delete a BGP redistribution profile. 

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
    api_instance = scm_network_services.BGPRedistributionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a BGP redistribution profile
        api_instance.delete_bgp_redistribution_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling BGPRedistributionProfilesApi->delete_bgp_redistribution_profiles_by_id: %s\n" % e)
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

# **get_bgp_redistribution_profiles_by_id**
> BgpRedistributionProfiles get_bgp_redistribution_profiles_by_id(id)

Get a BGP redistribution profile

Get an existing BGP redistribution profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.bgp_redistribution_profiles import BgpRedistributionProfiles
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
    api_instance = scm_network_services.BGPRedistributionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a BGP redistribution profile
        api_response = api_instance.get_bgp_redistribution_profiles_by_id(id)
        print("The response of BGPRedistributionProfilesApi->get_bgp_redistribution_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPRedistributionProfilesApi->get_bgp_redistribution_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**BgpRedistributionProfiles**](BgpRedistributionProfiles.md)

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

# **list_bgp_redistribution_profiles**
> BGPRedistributionProfilesListResponse list_bgp_redistribution_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List BGP redistribution profiles

Retrieve a list of BGP redistribution profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.bgp_redistribution_profiles_list_response import BGPRedistributionProfilesListResponse
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
    api_instance = scm_network_services.BGPRedistributionProfilesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List BGP redistribution profiles
        api_response = api_instance.list_bgp_redistribution_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of BGPRedistributionProfilesApi->list_bgp_redistribution_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPRedistributionProfilesApi->list_bgp_redistribution_profiles: %s\n" % e)
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

[**BGPRedistributionProfilesListResponse**](BGPRedistributionProfilesListResponse.md)

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

# **update_bgp_redistribution_profiles_by_id**
> BgpRedistributionProfiles update_bgp_redistribution_profiles_by_id(id, bgp_redistribution_profiles=bgp_redistribution_profiles)

Update a BGP redistribution profile

Update an existing BGP redistribution profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.bgp_redistribution_profiles import BgpRedistributionProfiles
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
    api_instance = scm_network_services.BGPRedistributionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    bgp_redistribution_profiles = scm_network_services.BgpRedistributionProfiles() # BgpRedistributionProfiles | OK (optional)

    try:
        # Update a BGP redistribution profile
        api_response = api_instance.update_bgp_redistribution_profiles_by_id(id, bgp_redistribution_profiles=bgp_redistribution_profiles)
        print("The response of BGPRedistributionProfilesApi->update_bgp_redistribution_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPRedistributionProfilesApi->update_bgp_redistribution_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **bgp_redistribution_profiles** | [**BgpRedistributionProfiles**](BgpRedistributionProfiles.md)| OK | [optional] 

### Return type

[**BgpRedistributionProfiles**](BgpRedistributionProfiles.md)

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

