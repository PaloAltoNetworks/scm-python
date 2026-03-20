# scm.config_setup.SharedSnippetsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_shared_snippets**](SharedSnippetsApi.md#convert_shared_snippets) | **PUT** /shared-snippets | Update Shared Snippets
[**list_shared_snippets**](SharedSnippetsApi.md#list_shared_snippets) | **GET** /shared-snippets | Get Shared Snippets
[**load_shared_snippets**](SharedSnippetsApi.md#load_shared_snippets) | **POST** /shared-snippets:load | Load Shared Snippets


# **convert_shared_snippets**
> SnippetShareInfo convert_shared_snippets(snippet_share_upload_payload=snippet_share_upload_payload)

Update Shared Snippets

Update Shared Snippets. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.snippet_share_info import SnippetShareInfo
from scm.config_setup.models.snippet_share_upload_payload import SnippetShareUploadPayload
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.SharedSnippetsApi(api_client)
    snippet_share_upload_payload = scm.config_setup.SnippetShareUploadPayload() # SnippetShareUploadPayload | The `Shared Snippets To Update` resource definition (optional)

    try:
        # Update Shared Snippets
        api_response = api_instance.convert_shared_snippets(snippet_share_upload_payload=snippet_share_upload_payload)
        print("The response of SharedSnippetsApi->convert_shared_snippets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedSnippetsApi->convert_shared_snippets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_share_upload_payload** | [**SnippetShareUploadPayload**](SnippetShareUploadPayload.md)| The &#x60;Shared Snippets To Update&#x60; resource definition | [optional] 

### Return type

[**SnippetShareInfo**](SnippetShareInfo.md)

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
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shared_snippets**
> List[SnippetShareInfo] list_shared_snippets()

Get Shared Snippets

Retrieve a list of shared snippets. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.snippet_share_info import SnippetShareInfo
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.SharedSnippetsApi(api_client)

    try:
        # Get Shared Snippets
        api_response = api_instance.list_shared_snippets()
        print("The response of SharedSnippetsApi->list_shared_snippets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedSnippetsApi->list_shared_snippets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SnippetShareInfo]**](SnippetShareInfo.md)

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

# **load_shared_snippets**
> SnippetShareLoadPayload load_shared_snippets(snippet_share_load_payload=snippet_share_load_payload)

Load Shared Snippets

Convert Snippet Snippets. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.snippet_share_load_payload import SnippetShareLoadPayload
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.SharedSnippetsApi(api_client)
    snippet_share_load_payload = scm.config_setup.SnippetShareLoadPayload() # SnippetShareLoadPayload | The `Snippet Snapshots To Convert` resource definition (optional)

    try:
        # Load Shared Snippets
        api_response = api_instance.load_shared_snippets(snippet_share_load_payload=snippet_share_load_payload)
        print("The response of SharedSnippetsApi->load_shared_snippets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedSnippetsApi->load_shared_snippets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_share_load_payload** | [**SnippetShareLoadPayload**](SnippetShareLoadPayload.md)| The &#x60;Snippet Snapshots To Convert&#x60; resource definition | [optional] 

### Return type

[**SnippetShareLoadPayload**](SnippetShareLoadPayload.md)

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
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

