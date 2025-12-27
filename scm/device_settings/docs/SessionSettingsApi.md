# scm_device_settings.SessionSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/device/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session_settings**](SessionSettingsApi.md#create_session_settings) | **POST** /session-settings | Create session settings
[**delete_session_settings_by_id**](SessionSettingsApi.md#delete_session_settings_by_id) | **DELETE** /session-settings/{id} | Delete session settings
[**get_session_settings_by_id**](SessionSettingsApi.md#get_session_settings_by_id) | **GET** /session-settings/{id} | Get existing session settings
[**list_session_settings**](SessionSettingsApi.md#list_session_settings) | **GET** /session-settings | List session settings
[**update_session_settings_by_id**](SessionSettingsApi.md#update_session_settings_by_id) | **PUT** /session-settings/{id} | Update session settings


# **create_session_settings**
> SessionSettings create_session_settings(session_settings=session_settings)

Create session settings

Create new session settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.session_settings import SessionSettings
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
    api_instance = scm_device_settings.SessionSettingsApi(api_client)
    session_settings = scm_device_settings.SessionSettings() # SessionSettings |  (optional)

    try:
        # Create session settings
        api_response = api_instance.create_session_settings(session_settings=session_settings)
        print("The response of SessionSettingsApi->create_session_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionSettingsApi->create_session_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_settings** | [**SessionSettings**](SessionSettings.md)|  | [optional] 

### Return type

[**SessionSettings**](SessionSettings.md)

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

# **delete_session_settings_by_id**
> delete_session_settings_by_id(id)

Delete session settings

Delete the session settings. 

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
    api_instance = scm_device_settings.SessionSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete session settings
        api_instance.delete_session_settings_by_id(id)
    except Exception as e:
        print("Exception when calling SessionSettingsApi->delete_session_settings_by_id: %s\n" % e)
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

# **get_session_settings_by_id**
> SessionSettings get_session_settings_by_id(id)

Get existing session settings

Retrieve existing session settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.session_settings import SessionSettings
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
    api_instance = scm_device_settings.SessionSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get existing session settings
        api_response = api_instance.get_session_settings_by_id(id)
        print("The response of SessionSettingsApi->get_session_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionSettingsApi->get_session_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**SessionSettings**](SessionSettings.md)

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

# **list_session_settings**
> List[SessionSettings] list_session_settings(folder=folder, snippet=snippet, device=device)

List session settings

Retrieve a list of session settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.session_settings import SessionSettings
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
    api_instance = scm_device_settings.SessionSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List session settings
        api_response = api_instance.list_session_settings(folder=folder, snippet=snippet, device=device)
        print("The response of SessionSettingsApi->list_session_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionSettingsApi->list_session_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**List[SessionSettings]**](SessionSettings.md)

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

# **update_session_settings_by_id**
> SessionSettings update_session_settings_by_id(id, session_settings=session_settings)

Update session settings

Update the session settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.session_settings import SessionSettings
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
    api_instance = scm_device_settings.SessionSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    session_settings = scm_device_settings.SessionSettings() # SessionSettings | OK (optional)

    try:
        # Update session settings
        api_response = api_instance.update_session_settings_by_id(id, session_settings=session_settings)
        print("The response of SessionSettingsApi->update_session_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionSettingsApi->update_session_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **session_settings** | [**SessionSettings**](SessionSettings.md)| OK | [optional] 

### Return type

[**SessionSettings**](SessionSettings.md)

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

