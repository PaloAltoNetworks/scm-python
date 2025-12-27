# scm.device_settings.UpdateScheduleSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/device/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_update_schedule_settings**](UpdateScheduleSettingsApi.md#create_update_schedule_settings) | **POST** /update-schedule | Create update schedule settings
[**delete_update_schedule_settings_by_id**](UpdateScheduleSettingsApi.md#delete_update_schedule_settings_by_id) | **DELETE** /update-schedule/{id} | Delete update schedule settings
[**get_update_schedule_settings_by_id**](UpdateScheduleSettingsApi.md#get_update_schedule_settings_by_id) | **GET** /update-schedule/{id} | Get existing update schedule settings
[**list_update_schedule_settings**](UpdateScheduleSettingsApi.md#list_update_schedule_settings) | **GET** /update-schedule | List update schedule settings
[**update_update_schedule_settings_by_id**](UpdateScheduleSettingsApi.md#update_update_schedule_settings_by_id) | **PUT** /update-schedule/{id} | Update update schedule settings


# **create_update_schedule_settings**
> UpdateSchedule create_update_schedule_settings(update_schedule=update_schedule)

Create update schedule settings

Create new update schedule settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.update_schedule import UpdateSchedule
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
    api_instance = scm.device_settings.UpdateScheduleSettingsApi(api_client)
    update_schedule = scm.device_settings.UpdateSchedule() # UpdateSchedule |  (optional)

    try:
        # Create update schedule settings
        api_response = api_instance.create_update_schedule_settings(update_schedule=update_schedule)
        print("The response of UpdateScheduleSettingsApi->create_update_schedule_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateScheduleSettingsApi->create_update_schedule_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_schedule** | [**UpdateSchedule**](UpdateSchedule.md)|  | [optional] 

### Return type

[**UpdateSchedule**](UpdateSchedule.md)

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

# **delete_update_schedule_settings_by_id**
> delete_update_schedule_settings_by_id(id)

Delete update schedule settings

Delete the update schedule settings. 

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
    api_instance = scm.device_settings.UpdateScheduleSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete update schedule settings
        api_instance.delete_update_schedule_settings_by_id(id)
    except Exception as e:
        print("Exception when calling UpdateScheduleSettingsApi->delete_update_schedule_settings_by_id: %s\n" % e)
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

# **get_update_schedule_settings_by_id**
> UpdateSchedule get_update_schedule_settings_by_id(id)

Get existing update schedule settings

Retrieve existing update schedule settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.update_schedule import UpdateSchedule
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
    api_instance = scm.device_settings.UpdateScheduleSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get existing update schedule settings
        api_response = api_instance.get_update_schedule_settings_by_id(id)
        print("The response of UpdateScheduleSettingsApi->get_update_schedule_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateScheduleSettingsApi->get_update_schedule_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**UpdateSchedule**](UpdateSchedule.md)

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

# **list_update_schedule_settings**
> List[UpdateSchedule] list_update_schedule_settings(folder=folder, snippet=snippet, device=device)

List update schedule settings

Retrieve a list of update schedule settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.update_schedule import UpdateSchedule
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
    api_instance = scm.device_settings.UpdateScheduleSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List update schedule settings
        api_response = api_instance.list_update_schedule_settings(folder=folder, snippet=snippet, device=device)
        print("The response of UpdateScheduleSettingsApi->list_update_schedule_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateScheduleSettingsApi->list_update_schedule_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**List[UpdateSchedule]**](UpdateSchedule.md)

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

# **update_update_schedule_settings_by_id**
> UpdateSchedule update_update_schedule_settings_by_id(id, update_schedule=update_schedule)

Update update schedule settings

Update the update schedule settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.update_schedule import UpdateSchedule
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
    api_instance = scm.device_settings.UpdateScheduleSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    update_schedule = scm.device_settings.UpdateSchedule() # UpdateSchedule | OK (optional)

    try:
        # Update update schedule settings
        api_response = api_instance.update_update_schedule_settings_by_id(id, update_schedule=update_schedule)
        print("The response of UpdateScheduleSettingsApi->update_update_schedule_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateScheduleSettingsApi->update_update_schedule_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **update_schedule** | [**UpdateSchedule**](UpdateSchedule.md)| OK | [optional] 

### Return type

[**UpdateSchedule**](UpdateSchedule.md)

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

