# scm.device_settings.DeviceRedistributionCollectorSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/device/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_redistribution_collector_settings**](DeviceRedistributionCollectorSettingsApi.md#create_device_redistribution_collector_settings) | **POST** /device-redistribution-collector | Create device redistribution collector settings
[**delete_device_redistribution_collector_settings_by_id**](DeviceRedistributionCollectorSettingsApi.md#delete_device_redistribution_collector_settings_by_id) | **DELETE** /device-redistribution-collector/{id} | Delete device redistribution collector settings
[**get_device_redistribution_collector_settings_by_id**](DeviceRedistributionCollectorSettingsApi.md#get_device_redistribution_collector_settings_by_id) | **GET** /device-redistribution-collector/{id} | Get existing device redistribution collector settings
[**list_device_redistribution_collector_settings**](DeviceRedistributionCollectorSettingsApi.md#list_device_redistribution_collector_settings) | **GET** /device-redistribution-collector | List device redistribution collector settings
[**update_device_redistribution_collector_settings_by_id**](DeviceRedistributionCollectorSettingsApi.md#update_device_redistribution_collector_settings_by_id) | **PUT** /device-redistribution-collector/{id} | Update device redistribution collector settings


# **create_device_redistribution_collector_settings**
> DeviceRedistributionCollector create_device_redistribution_collector_settings(device_redistribution_collector=device_redistribution_collector)

Create device redistribution collector settings

Create new device redistribution collector settings.

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.device_redistribution_collector import DeviceRedistributionCollector
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
    api_instance = scm.device_settings.DeviceRedistributionCollectorSettingsApi(api_client)
    device_redistribution_collector = scm.device_settings.DeviceRedistributionCollector() # DeviceRedistributionCollector |  (optional)

    try:
        # Create device redistribution collector settings
        api_response = api_instance.create_device_redistribution_collector_settings(device_redistribution_collector=device_redistribution_collector)
        print("The response of DeviceRedistributionCollectorSettingsApi->create_device_redistribution_collector_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceRedistributionCollectorSettingsApi->create_device_redistribution_collector_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_redistribution_collector** | [**DeviceRedistributionCollector**](DeviceRedistributionCollector.md)|  | [optional] 

### Return type

[**DeviceRedistributionCollector**](DeviceRedistributionCollector.md)

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

# **delete_device_redistribution_collector_settings_by_id**
> delete_device_redistribution_collector_settings_by_id(id)

Delete device redistribution collector settings

Delete the device redistribution collector settings. 

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
    api_instance = scm.device_settings.DeviceRedistributionCollectorSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete device redistribution collector settings
        api_instance.delete_device_redistribution_collector_settings_by_id(id)
    except Exception as e:
        print("Exception when calling DeviceRedistributionCollectorSettingsApi->delete_device_redistribution_collector_settings_by_id: %s\n" % e)
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

# **get_device_redistribution_collector_settings_by_id**
> DeviceRedistributionCollector get_device_redistribution_collector_settings_by_id(id)

Get existing device redistribution collector settings

Retrieve existing device redistribution collector settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.device_redistribution_collector import DeviceRedistributionCollector
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
    api_instance = scm.device_settings.DeviceRedistributionCollectorSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get existing device redistribution collector settings
        api_response = api_instance.get_device_redistribution_collector_settings_by_id(id)
        print("The response of DeviceRedistributionCollectorSettingsApi->get_device_redistribution_collector_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceRedistributionCollectorSettingsApi->get_device_redistribution_collector_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**DeviceRedistributionCollector**](DeviceRedistributionCollector.md)

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

# **list_device_redistribution_collector_settings**
> List[DeviceRedistributionCollector] list_device_redistribution_collector_settings(folder=folder, snippet=snippet, device=device)

List device redistribution collector settings

Retrieve a list of device redistribution collector settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.device_redistribution_collector import DeviceRedistributionCollector
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
    api_instance = scm.device_settings.DeviceRedistributionCollectorSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List device redistribution collector settings
        api_response = api_instance.list_device_redistribution_collector_settings(folder=folder, snippet=snippet, device=device)
        print("The response of DeviceRedistributionCollectorSettingsApi->list_device_redistribution_collector_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceRedistributionCollectorSettingsApi->list_device_redistribution_collector_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**List[DeviceRedistributionCollector]**](DeviceRedistributionCollector.md)

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

# **update_device_redistribution_collector_settings_by_id**
> DeviceRedistributionCollector update_device_redistribution_collector_settings_by_id(id, device_redistribution_collector=device_redistribution_collector)

Update device redistribution collector settings

Update the device redistribution collector settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.device_redistribution_collector import DeviceRedistributionCollector
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
    api_instance = scm.device_settings.DeviceRedistributionCollectorSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    device_redistribution_collector = scm.device_settings.DeviceRedistributionCollector() # DeviceRedistributionCollector | OK (optional)

    try:
        # Update device redistribution collector settings
        api_response = api_instance.update_device_redistribution_collector_settings_by_id(id, device_redistribution_collector=device_redistribution_collector)
        print("The response of DeviceRedistributionCollectorSettingsApi->update_device_redistribution_collector_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceRedistributionCollectorSettingsApi->update_device_redistribution_collector_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **device_redistribution_collector** | [**DeviceRedistributionCollector**](DeviceRedistributionCollector.md)| OK | [optional] 

### Return type

[**DeviceRedistributionCollector**](DeviceRedistributionCollector.md)

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

