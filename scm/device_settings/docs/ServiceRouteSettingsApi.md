# scm.device_settings.ServiceRouteSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/device/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_route_settings**](ServiceRouteSettingsApi.md#create_service_route_settings) | **POST** /service-route | Create service route settings
[**delete_service_route_settings_by_id**](ServiceRouteSettingsApi.md#delete_service_route_settings_by_id) | **DELETE** /service-route/{id} | Delete service route settings
[**get_service_route_settings_by_id**](ServiceRouteSettingsApi.md#get_service_route_settings_by_id) | **GET** /service-route/{id} | Get existing service route settings
[**list_service_route_settings**](ServiceRouteSettingsApi.md#list_service_route_settings) | **GET** /service-route | List service route settings
[**update_service_route_settings_by_id**](ServiceRouteSettingsApi.md#update_service_route_settings_by_id) | **PUT** /service-route/{id} | Update service route settings


# **create_service_route_settings**
> ServiceRoute create_service_route_settings(service_route=service_route)

Create service route settings

Create new service route settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.service_route import ServiceRoute
from scm.device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.device_settings.ServiceRouteSettingsApi(api_client)
    service_route = scm.device_settings.ServiceRoute() # ServiceRoute |  (optional)

    try:
        # Create service route settings
        api_response = api_instance.create_service_route_settings(service_route=service_route)
        print("The response of ServiceRouteSettingsApi->create_service_route_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceRouteSettingsApi->create_service_route_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_route** | [**ServiceRoute**](ServiceRoute.md)|  | [optional] 

### Return type

[**ServiceRoute**](ServiceRoute.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_route_settings_by_id**
> delete_service_route_settings_by_id(id)

Delete service route settings

Delete the service route settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.device_settings.ServiceRouteSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete service route settings
        api_instance.delete_service_route_settings_by_id(id)
    except Exception as e:
        print("Exception when calling ServiceRouteSettingsApi->delete_service_route_settings_by_id: %s\n" % e)
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

# **get_service_route_settings_by_id**
> ServiceRoute get_service_route_settings_by_id(id)

Get existing service route settings

Retrieve existing service route settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.service_route import ServiceRoute
from scm.device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.device_settings.ServiceRouteSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get existing service route settings
        api_response = api_instance.get_service_route_settings_by_id(id)
        print("The response of ServiceRouteSettingsApi->get_service_route_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceRouteSettingsApi->get_service_route_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**ServiceRoute**](ServiceRoute.md)

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

# **list_service_route_settings**
> List[ServiceRoute] list_service_route_settings(folder=folder, snippet=snippet, device=device)

List service route settings

Retrieve a list of service route settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.service_route import ServiceRoute
from scm.device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.device_settings.ServiceRouteSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List service route settings
        api_response = api_instance.list_service_route_settings(folder=folder, snippet=snippet, device=device)
        print("The response of ServiceRouteSettingsApi->list_service_route_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceRouteSettingsApi->list_service_route_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**List[ServiceRoute]**](ServiceRoute.md)

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

# **update_service_route_settings_by_id**
> ServiceRoute update_service_route_settings_by_id(id, service_route=service_route)

Update service route settings

Update the service route settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.service_route import ServiceRoute
from scm.device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.device_settings.ServiceRouteSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    service_route = scm.device_settings.ServiceRoute() # ServiceRoute | OK (optional)

    try:
        # Update service route settings
        api_response = api_instance.update_service_route_settings_by_id(id, service_route=service_route)
        print("The response of ServiceRouteSettingsApi->update_service_route_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceRouteSettingsApi->update_service_route_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **service_route** | [**ServiceRoute**](ServiceRoute.md)| OK | [optional] 

### Return type

[**ServiceRoute**](ServiceRoute.md)

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

