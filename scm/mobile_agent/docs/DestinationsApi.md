# scm.mobile_agent.DestinationsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/mobile-agent/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_protect_destination**](DestinationsApi.md#create_global_protect_destination) | **POST** /forwarding-profile-destinations | Create a GlobalProtect destination
[**delete_global_protect_destination**](DestinationsApi.md#delete_global_protect_destination) | **DELETE** /forwarding-profile-destinations/{id} | Delete a GlobalProtect destination
[**get_global_protect_destination_by_id**](DestinationsApi.md#get_global_protect_destination_by_id) | **GET** /forwarding-profile-destinations/{id} | Get a GlobalProtect destination
[**list_global_protect_destinations**](DestinationsApi.md#list_global_protect_destinations) | **GET** /forwarding-profile-destinations | List GlobalProtect destinations
[**update_global_protect_destination_by_id**](DestinationsApi.md#update_global_protect_destination_by_id) | **PUT** /forwarding-profile-destinations/{id} | Update a GlobalProtect destination


# **create_global_protect_destination**
> ForwardingProfileDestinations create_global_protect_destination(folder=folder, forwarding_profile_destinations=forwarding_profile_destinations)

Create a GlobalProtect destination

Create a new GlobalProtect destination 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_destinations import ForwardingProfileDestinations
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
    api_instance = scm.mobile_agent.DestinationsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    forwarding_profile_destinations = scm.mobile_agent.ForwardingProfileDestinations() # ForwardingProfileDestinations | Created (optional)

    try:
        # Create a GlobalProtect destination
        api_response = api_instance.create_global_protect_destination(folder=folder, forwarding_profile_destinations=forwarding_profile_destinations)
        print("The response of DestinationsApi->create_global_protect_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->create_global_protect_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **forwarding_profile_destinations** | [**ForwardingProfileDestinations**](ForwardingProfileDestinations.md)| Created | [optional] 

### Return type

[**ForwardingProfileDestinations**](ForwardingProfileDestinations.md)

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

# **delete_global_protect_destination**
> delete_global_protect_destination(id)

Delete a GlobalProtect destination

Delete a GlobalProtect destination 

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
    api_instance = scm.mobile_agent.DestinationsApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Delete a GlobalProtect destination
        api_instance.delete_global_protect_destination(id)
    except Exception as e:
        print("Exception when calling DestinationsApi->delete_global_protect_destination: %s\n" % e)
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

# **get_global_protect_destination_by_id**
> ForwardingProfileDestinations get_global_protect_destination_by_id(id)

Get a GlobalProtect destination

Retrieve an existing GlobalProtect destination 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_destinations import ForwardingProfileDestinations
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
    api_instance = scm.mobile_agent.DestinationsApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get a GlobalProtect destination
        api_response = api_instance.get_global_protect_destination_by_id(id)
        print("The response of DestinationsApi->get_global_protect_destination_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->get_global_protect_destination_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**ForwardingProfileDestinations**](ForwardingProfileDestinations.md)

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

# **list_global_protect_destinations**
> GlobalProtectDestinationsListResponse list_global_protect_destinations(name=name, limit=limit, offset=offset, folder=folder)

List GlobalProtect destinations

Retrieve a list of GlobalProtect destinations 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.global_protect_destinations_list_response import GlobalProtectDestinationsListResponse
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
    api_instance = scm.mobile_agent.DestinationsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)

    try:
        # List GlobalProtect destinations
        api_response = api_instance.list_global_protect_destinations(name=name, limit=limit, offset=offset, folder=folder)
        print("The response of DestinationsApi->list_global_protect_destinations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->list_global_protect_destinations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **folder** | **str**| The folder in which the resource is defined  | [optional] 

### Return type

[**GlobalProtectDestinationsListResponse**](GlobalProtectDestinationsListResponse.md)

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

# **update_global_protect_destination_by_id**
> ForwardingProfileDestinations update_global_protect_destination_by_id(id, forwarding_profile_destinations=forwarding_profile_destinations)

Update a GlobalProtect destination

Update an existing GlobalProtect destination 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.mobile_agent
from scm.mobile_agent.models.forwarding_profile_destinations import ForwardingProfileDestinations
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
    api_instance = scm.mobile_agent.DestinationsApi(api_client)
    id = 'id_example' # str | The UUID of the resource
    forwarding_profile_destinations = scm.mobile_agent.ForwardingProfileDestinations() # ForwardingProfileDestinations | The destination resource definition (optional)

    try:
        # Update a GlobalProtect destination
        api_response = api_instance.update_global_protect_destination_by_id(id, forwarding_profile_destinations=forwarding_profile_destinations)
        print("The response of DestinationsApi->update_global_protect_destination_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->update_global_protect_destination_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 
 **forwarding_profile_destinations** | [**ForwardingProfileDestinations**](ForwardingProfileDestinations.md)| The destination resource definition | [optional] 

### Return type

[**ForwardingProfileDestinations**](ForwardingProfileDestinations.md)

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

