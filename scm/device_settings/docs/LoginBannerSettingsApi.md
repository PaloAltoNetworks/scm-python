# scm_device_settings.LoginBannerSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/device/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_login_banner_settings**](LoginBannerSettingsApi.md#create_login_banner_settings) | **POST** /motd-banner-settings | Create login banner settings
[**delete_login_banner_settings_by_id**](LoginBannerSettingsApi.md#delete_login_banner_settings_by_id) | **DELETE** /motd-banner-settings/{id} | Delete login banner settings
[**get_login_banner_settings_by_id**](LoginBannerSettingsApi.md#get_login_banner_settings_by_id) | **GET** /motd-banner-settings/{id} | Get existing login banner settings
[**list_login_banner_settings**](LoginBannerSettingsApi.md#list_login_banner_settings) | **GET** /motd-banner-settings | List login banner settings
[**update_login_banner_settings_by_id**](LoginBannerSettingsApi.md#update_login_banner_settings_by_id) | **PUT** /motd-banner-settings/{id} | Update login banner settings


# **create_login_banner_settings**
> MotdBannerSettings create_login_banner_settings(motd_banner_settings=motd_banner_settings)

Create login banner settings

Create new login banner settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.motd_banner_settings import MotdBannerSettings
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
    api_instance = scm_device_settings.LoginBannerSettingsApi(api_client)
    motd_banner_settings = scm_device_settings.MotdBannerSettings() # MotdBannerSettings |  (optional)

    try:
        # Create login banner settings
        api_response = api_instance.create_login_banner_settings(motd_banner_settings=motd_banner_settings)
        print("The response of LoginBannerSettingsApi->create_login_banner_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginBannerSettingsApi->create_login_banner_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **motd_banner_settings** | [**MotdBannerSettings**](MotdBannerSettings.md)|  | [optional] 

### Return type

[**MotdBannerSettings**](MotdBannerSettings.md)

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

# **delete_login_banner_settings_by_id**
> delete_login_banner_settings_by_id(id)

Delete login banner settings

Delete the login banner settings. 

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
    api_instance = scm_device_settings.LoginBannerSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete login banner settings
        api_instance.delete_login_banner_settings_by_id(id)
    except Exception as e:
        print("Exception when calling LoginBannerSettingsApi->delete_login_banner_settings_by_id: %s\n" % e)
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

# **get_login_banner_settings_by_id**
> MotdBannerSettings get_login_banner_settings_by_id(id)

Get existing login banner settings

Retrieve existing login banner settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.motd_banner_settings import MotdBannerSettings
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
    api_instance = scm_device_settings.LoginBannerSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get existing login banner settings
        api_response = api_instance.get_login_banner_settings_by_id(id)
        print("The response of LoginBannerSettingsApi->get_login_banner_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginBannerSettingsApi->get_login_banner_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**MotdBannerSettings**](MotdBannerSettings.md)

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

# **list_login_banner_settings**
> List[MotdBannerSettings] list_login_banner_settings(folder=folder, snippet=snippet, device=device)

List login banner settings

Retrieve a list of login banner settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.motd_banner_settings import MotdBannerSettings
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
    api_instance = scm_device_settings.LoginBannerSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List login banner settings
        api_response = api_instance.list_login_banner_settings(folder=folder, snippet=snippet, device=device)
        print("The response of LoginBannerSettingsApi->list_login_banner_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginBannerSettingsApi->list_login_banner_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**List[MotdBannerSettings]**](MotdBannerSettings.md)

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

# **update_login_banner_settings_by_id**
> MotdBannerSettings update_login_banner_settings_by_id(id, motd_banner_settings=motd_banner_settings)

Update login banner settings

Update the login banner settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.motd_banner_settings import MotdBannerSettings
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
    api_instance = scm_device_settings.LoginBannerSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    motd_banner_settings = scm_device_settings.MotdBannerSettings() # MotdBannerSettings | OK (optional)

    try:
        # Update login banner settings
        api_response = api_instance.update_login_banner_settings_by_id(id, motd_banner_settings=motd_banner_settings)
        print("The response of LoginBannerSettingsApi->update_login_banner_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginBannerSettingsApi->update_login_banner_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **motd_banner_settings** | [**MotdBannerSettings**](MotdBannerSettings.md)| OK | [optional] 

### Return type

[**MotdBannerSettings**](MotdBannerSettings.md)

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

