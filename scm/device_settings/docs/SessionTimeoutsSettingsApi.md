# scm_device_settings.SessionTimeoutsSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/device/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session_timeouts_settings**](SessionTimeoutsSettingsApi.md#create_session_timeouts_settings) | **POST** /session-timeouts | Create session timeouts settings
[**delete_session_timeouts_settings_by_id**](SessionTimeoutsSettingsApi.md#delete_session_timeouts_settings_by_id) | **DELETE** /session-timeouts/{id} | Delete session settings
[**get_session_timeouts_settings_by_id**](SessionTimeoutsSettingsApi.md#get_session_timeouts_settings_by_id) | **GET** /session-timeouts/{id} | Get existing session settings
[**list_session_timeouts_settings**](SessionTimeoutsSettingsApi.md#list_session_timeouts_settings) | **GET** /session-timeouts | List session timeouts settings
[**update_session_timeouts_settings_by_id**](SessionTimeoutsSettingsApi.md#update_session_timeouts_settings_by_id) | **PUT** /session-timeouts/{id} | Update session settings


# **create_session_timeouts_settings**
> SessionTimeouts create_session_timeouts_settings(session_timeouts=session_timeouts)

Create session timeouts settings

Create new session timeouts settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.session_timeouts import SessionTimeouts
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
    api_instance = scm_device_settings.SessionTimeoutsSettingsApi(api_client)
    session_timeouts = scm_device_settings.SessionTimeouts() # SessionTimeouts |  (optional)

    try:
        # Create session timeouts settings
        api_response = api_instance.create_session_timeouts_settings(session_timeouts=session_timeouts)
        print("The response of SessionTimeoutsSettingsApi->create_session_timeouts_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionTimeoutsSettingsApi->create_session_timeouts_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_timeouts** | [**SessionTimeouts**](SessionTimeouts.md)|  | [optional] 

### Return type

[**SessionTimeouts**](SessionTimeouts.md)

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

# **delete_session_timeouts_settings_by_id**
> delete_session_timeouts_settings_by_id(id)

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
    api_instance = scm_device_settings.SessionTimeoutsSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete session settings
        api_instance.delete_session_timeouts_settings_by_id(id)
    except Exception as e:
        print("Exception when calling SessionTimeoutsSettingsApi->delete_session_timeouts_settings_by_id: %s\n" % e)
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

# **get_session_timeouts_settings_by_id**
> SessionTimeouts get_session_timeouts_settings_by_id(id)

Get existing session settings

Retrieve existing session settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.session_timeouts import SessionTimeouts
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
    api_instance = scm_device_settings.SessionTimeoutsSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get existing session settings
        api_response = api_instance.get_session_timeouts_settings_by_id(id)
        print("The response of SessionTimeoutsSettingsApi->get_session_timeouts_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionTimeoutsSettingsApi->get_session_timeouts_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**SessionTimeouts**](SessionTimeouts.md)

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

# **list_session_timeouts_settings**
> List[SessionTimeouts] list_session_timeouts_settings(folder=folder, snippet=snippet, device=device)

List session timeouts settings

Retrieve a list of session timeouts settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.session_timeouts import SessionTimeouts
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
    api_instance = scm_device_settings.SessionTimeoutsSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List session timeouts settings
        api_response = api_instance.list_session_timeouts_settings(folder=folder, snippet=snippet, device=device)
        print("The response of SessionTimeoutsSettingsApi->list_session_timeouts_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionTimeoutsSettingsApi->list_session_timeouts_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**List[SessionTimeouts]**](SessionTimeouts.md)

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

# **update_session_timeouts_settings_by_id**
> SessionTimeouts update_session_timeouts_settings_by_id(id, session_timeouts=session_timeouts)

Update session settings

Update the session settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.session_timeouts import SessionTimeouts
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
    api_instance = scm_device_settings.SessionTimeoutsSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    session_timeouts = scm_device_settings.SessionTimeouts() # SessionTimeouts | OK (optional)

    try:
        # Update session settings
        api_response = api_instance.update_session_timeouts_settings_by_id(id, session_timeouts=session_timeouts)
        print("The response of SessionTimeoutsSettingsApi->update_session_timeouts_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionTimeoutsSettingsApi->update_session_timeouts_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **session_timeouts** | [**SessionTimeouts**](SessionTimeouts.md)| OK | [optional] 

### Return type

[**SessionTimeouts**](SessionTimeouts.md)

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

