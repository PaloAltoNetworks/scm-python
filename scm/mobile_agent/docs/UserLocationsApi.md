# scm.mobile_agent.UserLocationsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/mobile-agent/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_protect_user_location**](UserLocationsApi.md#create_global_protect_user_location) | **POST** /forwarding-profile-user-locations | Create a GlobalProtect user location
[**delete_global_protect_user_location**](UserLocationsApi.md#delete_global_protect_user_location) | **DELETE** /forwarding-profile-user-locations/{id} | Delete a GlobalProtect user location
[**get_global_protect_user_location_by_id**](UserLocationsApi.md#get_global_protect_user_location_by_id) | **GET** /forwarding-profile-user-locations/{id} | Get a GlobalProtect user location
[**list_global_protect_user_locations**](UserLocationsApi.md#list_global_protect_user_locations) | **GET** /forwarding-profile-user-locations | List GlobalProtect user locations
[**update_global_protect_user_location_by_id**](UserLocationsApi.md#update_global_protect_user_location_by_id) | **PUT** /forwarding-profile-user-locations/{id} | Update a GlobalProtect user location


# **create_global_protect_user_location**
> ForwardingProfileUserLocations create_global_protect_user_location(folder=folder, forwarding_profile_user_locations=forwarding_profile_user_locations)

Create a GlobalProtect user location

Create a new GlobalProtect user location 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_user_locations import ForwardingProfileUserLocations
from scm.mobile_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.mobile_agent.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/mobile-agent/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.mobile_agent.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.mobile_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.mobile_agent.UserLocationsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    forwarding_profile_user_locations = scm.mobile_agent.ForwardingProfileUserLocations() # ForwardingProfileUserLocations | Created (optional)

    try:
        # Create a GlobalProtect user location
        api_response = api_instance.create_global_protect_user_location(folder=folder, forwarding_profile_user_locations=forwarding_profile_user_locations)
        print("The response of UserLocationsApi->create_global_protect_user_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLocationsApi->create_global_protect_user_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **forwarding_profile_user_locations** | [**ForwardingProfileUserLocations**](ForwardingProfileUserLocations.md)| Created | [optional] 

### Return type

[**ForwardingProfileUserLocations**](ForwardingProfileUserLocations.md)

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

# **delete_global_protect_user_location**
> delete_global_protect_user_location(id)

Delete a GlobalProtect user location

Delete a GlobalProtect user location 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.mobile_agent.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/mobile-agent/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.mobile_agent.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.mobile_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.mobile_agent.UserLocationsApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Delete a GlobalProtect user location
        api_instance.delete_global_protect_user_location(id)
    except Exception as e:
        print("Exception when calling UserLocationsApi->delete_global_protect_user_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

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

# **get_global_protect_user_location_by_id**
> ForwardingProfileUserLocations get_global_protect_user_location_by_id(id)

Get a GlobalProtect user location

Retrieve an existing GlobalProtect user location 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_user_locations import ForwardingProfileUserLocations
from scm.mobile_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.mobile_agent.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/mobile-agent/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.mobile_agent.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.mobile_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.mobile_agent.UserLocationsApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get a GlobalProtect user location
        api_response = api_instance.get_global_protect_user_location_by_id(id)
        print("The response of UserLocationsApi->get_global_protect_user_location_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLocationsApi->get_global_protect_user_location_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**ForwardingProfileUserLocations**](ForwardingProfileUserLocations.md)

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

# **list_global_protect_user_locations**
> GlobalProtectUserLocationsListResponse list_global_protect_user_locations(name=name, limit=limit, offset=offset, folder=folder)

List GlobalProtect user locations

Retrieve a list of GlobalProtect user locations 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.global_protect_user_locations_list_response import GlobalProtectUserLocationsListResponse
from scm.mobile_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.mobile_agent.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/mobile-agent/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.mobile_agent.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.mobile_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.mobile_agent.UserLocationsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)

    try:
        # List GlobalProtect user locations
        api_response = api_instance.list_global_protect_user_locations(name=name, limit=limit, offset=offset, folder=folder)
        print("The response of UserLocationsApi->list_global_protect_user_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLocationsApi->list_global_protect_user_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **folder** | **str**| The folder in which the resource is defined  | [optional] 

### Return type

[**GlobalProtectUserLocationsListResponse**](GlobalProtectUserLocationsListResponse.md)

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

# **update_global_protect_user_location_by_id**
> ForwardingProfileUserLocations update_global_protect_user_location_by_id(id, forwarding_profile_user_locations=forwarding_profile_user_locations)

Update a GlobalProtect user location

Update an existing GlobalProtect user location 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_user_locations import ForwardingProfileUserLocations
from scm.mobile_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.mobile_agent.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/mobile-agent/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.mobile_agent.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.mobile_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.mobile_agent.UserLocationsApi(api_client)
    id = 'id_example' # str | The UUID of the resource
    forwarding_profile_user_locations = scm.mobile_agent.ForwardingProfileUserLocations() # ForwardingProfileUserLocations | The user location resource definition (optional)

    try:
        # Update a GlobalProtect user location
        api_response = api_instance.update_global_protect_user_location_by_id(id, forwarding_profile_user_locations=forwarding_profile_user_locations)
        print("The response of UserLocationsApi->update_global_protect_user_location_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLocationsApi->update_global_protect_user_location_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 
 **forwarding_profile_user_locations** | [**ForwardingProfileUserLocations**](ForwardingProfileUserLocations.md)| The user location resource definition | [optional] 

### Return type

[**ForwardingProfileUserLocations**](ForwardingProfileUserLocations.md)

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

