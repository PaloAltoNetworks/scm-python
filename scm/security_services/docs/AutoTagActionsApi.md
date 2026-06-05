# scm.security_services.AutoTagActionsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_tag_actions**](AutoTagActionsApi.md#create_auto_tag_actions) | **POST** /auto-tag-actions | Create an auto-tag action
[**delete_auto_tag_actions**](AutoTagActionsApi.md#delete_auto_tag_actions) | **DELETE** /auto-tag-actions | Delete an Auto-Tag action
[**list_auto_tag_actions**](AutoTagActionsApi.md#list_auto_tag_actions) | **GET** /auto-tag-actions | List auto-tag actions
[**update_auto_tag_actions**](AutoTagActionsApi.md#update_auto_tag_actions) | **PUT** /auto-tag-actions | Update an auto-tag action


# **create_auto_tag_actions**
> AutoTagActions create_auto_tag_actions(auto_tag_actions=auto_tag_actions)

Create an auto-tag action

Create a new auto-tag action. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.auto_tag_actions import AutoTagActions
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.AutoTagActionsApi(api_client)
    auto_tag_actions = scm.security_services.AutoTagActions() # AutoTagActions | Created (optional)

    try:
        # Create an auto-tag action
        api_response = api_instance.create_auto_tag_actions(auto_tag_actions=auto_tag_actions)
        print("The response of AutoTagActionsApi->create_auto_tag_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTagActionsApi->create_auto_tag_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_tag_actions** | [**AutoTagActions**](AutoTagActions.md)| Created | [optional] 

### Return type

[**AutoTagActions**](AutoTagActions.md)

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

# **delete_auto_tag_actions**
> delete_auto_tag_actions(name)

Delete an Auto-Tag action

Delete an auto-tag action.

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.AutoTagActionsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource

    try:
        # Delete an Auto-Tag action
        api_instance.delete_auto_tag_actions(name)
    except Exception as e:
        print("Exception when calling AutoTagActionsApi->delete_auto_tag_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | 

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

# **list_auto_tag_actions**
> AutoTagActionsListResponse list_auto_tag_actions(name=name, offset=offset, limit=limit)

List auto-tag actions

Retrieve a list of auto-tag actions 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.auto_tag_actions_list_response import AutoTagActionsListResponse
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.AutoTagActionsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List auto-tag actions
        api_response = api_instance.list_auto_tag_actions(name=name, offset=offset, limit=limit)
        print("The response of AutoTagActionsApi->list_auto_tag_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTagActionsApi->list_auto_tag_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]

### Return type

[**AutoTagActionsListResponse**](AutoTagActionsListResponse.md)

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

# **update_auto_tag_actions**
> AutoTagActions update_auto_tag_actions(auto_tag_actions=auto_tag_actions)

Update an auto-tag action

Update an existing auto-tag action. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.auto_tag_actions import AutoTagActions
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.AutoTagActionsApi(api_client)
    auto_tag_actions = scm.security_services.AutoTagActions() # AutoTagActions | OK (optional)

    try:
        # Update an auto-tag action
        api_response = api_instance.update_auto_tag_actions(auto_tag_actions=auto_tag_actions)
        print("The response of AutoTagActionsApi->update_auto_tag_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTagActionsApi->update_auto_tag_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_tag_actions** | [**AutoTagActions**](AutoTagActions.md)| OK | [optional] 

### Return type

[**AutoTagActions**](AutoTagActions.md)

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

