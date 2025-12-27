# scm_device_settings.AuthenticationSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/device/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authentication_settings**](AuthenticationSettingsApi.md#create_authentication_settings) | **POST** /authentication-settings | Create authentication settings
[**delete_authentication_settings_by_id**](AuthenticationSettingsApi.md#delete_authentication_settings_by_id) | **DELETE** /authentication-settings/{id} | Delete authentication settings
[**get_authentication_settings_by_id**](AuthenticationSettingsApi.md#get_authentication_settings_by_id) | **GET** /authentication-settings/{id} | Get existing authentication settings
[**list_authentication_settings**](AuthenticationSettingsApi.md#list_authentication_settings) | **GET** /authentication-settings | List authentication settings
[**update_authentication_settings_by_id**](AuthenticationSettingsApi.md#update_authentication_settings_by_id) | **PUT** /authentication-settings/{id} | Update authentication settings


# **create_authentication_settings**
> AuthenticationSettings create_authentication_settings(authentication_settings=authentication_settings)

Create authentication settings

Create new device authentication settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.authentication_settings import AuthenticationSettings
from scm_device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_device_settings.AuthenticationSettingsApi(api_client)
    authentication_settings = scm_device_settings.AuthenticationSettings() # AuthenticationSettings |  (optional)

    try:
        # Create authentication settings
        api_response = api_instance.create_authentication_settings(authentication_settings=authentication_settings)
        print("The response of AuthenticationSettingsApi->create_authentication_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationSettingsApi->create_authentication_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_settings** | [**AuthenticationSettings**](AuthenticationSettings.md)|  | [optional] 

### Return type

[**AuthenticationSettings**](AuthenticationSettings.md)

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

# **delete_authentication_settings_by_id**
> delete_authentication_settings_by_id(id)

Delete authentication settings

Delete the device authentication settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_device_settings.AuthenticationSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete authentication settings
        api_instance.delete_authentication_settings_by_id(id)
    except Exception as e:
        print("Exception when calling AuthenticationSettingsApi->delete_authentication_settings_by_id: %s\n" % e)
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

# **get_authentication_settings_by_id**
> AuthenticationSettings get_authentication_settings_by_id(id)

Get existing authentication settings

Retrieve existing device authentication settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.authentication_settings import AuthenticationSettings
from scm_device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_device_settings.AuthenticationSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get existing authentication settings
        api_response = api_instance.get_authentication_settings_by_id(id)
        print("The response of AuthenticationSettingsApi->get_authentication_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationSettingsApi->get_authentication_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**AuthenticationSettings**](AuthenticationSettings.md)

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

# **list_authentication_settings**
> List[AuthenticationSettings] list_authentication_settings(folder=folder, snippet=snippet, device=device)

List authentication settings

Retrieve a list of device authentication settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.authentication_settings import AuthenticationSettings
from scm_device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_device_settings.AuthenticationSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List authentication settings
        api_response = api_instance.list_authentication_settings(folder=folder, snippet=snippet, device=device)
        print("The response of AuthenticationSettingsApi->list_authentication_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationSettingsApi->list_authentication_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**List[AuthenticationSettings]**](AuthenticationSettings.md)

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

# **update_authentication_settings_by_id**
> AuthenticationSettings update_authentication_settings_by_id(id, authentication_settings=authentication_settings)

Update authentication settings

Update the device authentication settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.authentication_settings import AuthenticationSettings
from scm_device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_device_settings.AuthenticationSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    authentication_settings = scm_device_settings.AuthenticationSettings() # AuthenticationSettings |  (optional)

    try:
        # Update authentication settings
        api_response = api_instance.update_authentication_settings_by_id(id, authentication_settings=authentication_settings)
        print("The response of AuthenticationSettingsApi->update_authentication_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationSettingsApi->update_authentication_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **authentication_settings** | [**AuthenticationSettings**](AuthenticationSettings.md)|  | [optional] 

### Return type

[**AuthenticationSettings**](AuthenticationSettings.md)

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

