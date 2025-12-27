# scm.device_settings.ContentIDSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/device/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_content_id_settings**](ContentIDSettingsApi.md#create_content_id_settings) | **POST** /content-id-settings | Create Content-ID settings
[**delete_content_id_settings_by_id**](ContentIDSettingsApi.md#delete_content_id_settings_by_id) | **DELETE** /content-id-settings/{id} | Delete Content-ID settings
[**get_content_id_settings_by_id**](ContentIDSettingsApi.md#get_content_id_settings_by_id) | **GET** /content-id-settings/{id} | Get existing Content-ID settings
[**list_content_id_settings**](ContentIDSettingsApi.md#list_content_id_settings) | **GET** /content-id-settings | List Content-ID settings
[**update_content_id_settings_by_id**](ContentIDSettingsApi.md#update_content_id_settings_by_id) | **PUT** /content-id-settings/{id} | Update Content-ID settings


# **create_content_id_settings**
> ContentIdSettings create_content_id_settings(content_id_settings=content_id_settings)

Create Content-ID settings

Create new Content-ID settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.content_id_settings import ContentIdSettings
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
    api_instance = scm.device_settings.ContentIDSettingsApi(api_client)
    content_id_settings = scm.device_settings.ContentIdSettings() # ContentIdSettings |  (optional)

    try:
        # Create Content-ID settings
        api_response = api_instance.create_content_id_settings(content_id_settings=content_id_settings)
        print("The response of ContentIDSettingsApi->create_content_id_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentIDSettingsApi->create_content_id_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id_settings** | [**ContentIdSettings**](ContentIdSettings.md)|  | [optional] 

### Return type

[**ContentIdSettings**](ContentIdSettings.md)

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

# **delete_content_id_settings_by_id**
> delete_content_id_settings_by_id(id)

Delete Content-ID settings

Delete the Content-ID settings. 

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
    api_instance = scm.device_settings.ContentIDSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete Content-ID settings
        api_instance.delete_content_id_settings_by_id(id)
    except Exception as e:
        print("Exception when calling ContentIDSettingsApi->delete_content_id_settings_by_id: %s\n" % e)
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

# **get_content_id_settings_by_id**
> ContentIdSettings get_content_id_settings_by_id(id)

Get existing Content-ID settings

Retrieve existing Content-ID settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.content_id_settings import ContentIdSettings
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
    api_instance = scm.device_settings.ContentIDSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get existing Content-ID settings
        api_response = api_instance.get_content_id_settings_by_id(id)
        print("The response of ContentIDSettingsApi->get_content_id_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentIDSettingsApi->get_content_id_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**ContentIdSettings**](ContentIdSettings.md)

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

# **list_content_id_settings**
> List[ContentIdSettings] list_content_id_settings(folder=folder, snippet=snippet, device=device)

List Content-ID settings

Retrieve a list of Content-ID settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.content_id_settings import ContentIdSettings
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
    api_instance = scm.device_settings.ContentIDSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List Content-ID settings
        api_response = api_instance.list_content_id_settings(folder=folder, snippet=snippet, device=device)
        print("The response of ContentIDSettingsApi->list_content_id_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentIDSettingsApi->list_content_id_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**List[ContentIdSettings]**](ContentIdSettings.md)

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

# **update_content_id_settings_by_id**
> ContentIdSettings update_content_id_settings_by_id(id, content_id_settings=content_id_settings)

Update Content-ID settings

Update the Content-ID settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.device_settings
from scm.device_settings.models.content_id_settings import ContentIdSettings
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
    api_instance = scm.device_settings.ContentIDSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    content_id_settings = scm.device_settings.ContentIdSettings() # ContentIdSettings | OK (optional)

    try:
        # Update Content-ID settings
        api_response = api_instance.update_content_id_settings_by_id(id, content_id_settings=content_id_settings)
        print("The response of ContentIDSettingsApi->update_content_id_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentIDSettingsApi->update_content_id_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **content_id_settings** | [**ContentIdSettings**](ContentIdSettings.md)| OK | [optional] 

### Return type

[**ContentIdSettings**](ContentIdSettings.md)

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

