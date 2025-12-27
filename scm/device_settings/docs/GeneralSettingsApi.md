# scm.device_settings.GeneralSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/device/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**creeate_general_settings**](GeneralSettingsApi.md#creeate_general_settings) | **POST** /general-settings | Create general settings
[**delete_general_settings_by_id**](GeneralSettingsApi.md#delete_general_settings_by_id) | **DELETE** /general-settings/{id} | Delete general settings
[**get_general_settings_by_id**](GeneralSettingsApi.md#get_general_settings_by_id) | **GET** /general-settings/{id} | Get existing general settings
[**list_general_settings**](GeneralSettingsApi.md#list_general_settings) | **GET** /general-settings | List general settings
[**update_general_settings_by_id**](GeneralSettingsApi.md#update_general_settings_by_id) | **PUT** /general-settings/{id} | Update general settings


# **creeate_general_settings**
> GeneralSettings creeate_general_settings(general_settings=general_settings)

Create general settings

Create new general settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.general_settings import GeneralSettings
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
    api_instance = scm.device_settings.GeneralSettingsApi(api_client)
    general_settings = scm.device_settings.GeneralSettings() # GeneralSettings |  (optional)

    try:
        # Create general settings
        api_response = api_instance.creeate_general_settings(general_settings=general_settings)
        print("The response of GeneralSettingsApi->creeate_general_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralSettingsApi->creeate_general_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **general_settings** | [**GeneralSettings**](GeneralSettings.md)|  | [optional] 

### Return type

[**GeneralSettings**](GeneralSettings.md)

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

# **delete_general_settings_by_id**
> delete_general_settings_by_id(id)

Delete general settings

Delete the general settings. 

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
    api_instance = scm.device_settings.GeneralSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete general settings
        api_instance.delete_general_settings_by_id(id)
    except Exception as e:
        print("Exception when calling GeneralSettingsApi->delete_general_settings_by_id: %s\n" % e)
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

# **get_general_settings_by_id**
> GeneralSettings get_general_settings_by_id(id)

Get existing general settings

Retrieve existing general settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.general_settings import GeneralSettings
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
    api_instance = scm.device_settings.GeneralSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get existing general settings
        api_response = api_instance.get_general_settings_by_id(id)
        print("The response of GeneralSettingsApi->get_general_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralSettingsApi->get_general_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**GeneralSettings**](GeneralSettings.md)

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

# **list_general_settings**
> List[GeneralSettings] list_general_settings(folder=folder, snippet=snippet, device=device)

List general settings

Retrieve a list of general settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.general_settings import GeneralSettings
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
    api_instance = scm.device_settings.GeneralSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List general settings
        api_response = api_instance.list_general_settings(folder=folder, snippet=snippet, device=device)
        print("The response of GeneralSettingsApi->list_general_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralSettingsApi->list_general_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**List[GeneralSettings]**](GeneralSettings.md)

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

# **update_general_settings_by_id**
> GeneralSettings update_general_settings_by_id(id, general_settings=general_settings)

Update general settings

Update the device redistribution collector settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.general_settings import GeneralSettings
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
    api_instance = scm.device_settings.GeneralSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    general_settings = scm.device_settings.GeneralSettings() # GeneralSettings | OK (optional)

    try:
        # Update general settings
        api_response = api_instance.update_general_settings_by_id(id, general_settings=general_settings)
        print("The response of GeneralSettingsApi->update_general_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralSettingsApi->update_general_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **general_settings** | [**GeneralSettings**](GeneralSettings.md)| OK | [optional] 

### Return type

[**GeneralSettings**](GeneralSettings.md)

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

