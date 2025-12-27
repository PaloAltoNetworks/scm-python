# scm.config_setup.SnippetCategoriesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_snippet_category_by_id**](SnippetCategoriesApi.md#delete_snippet_category_by_id) | **DELETE** /snippet-categories/{id} | Delete a snippet category
[**get_snippet_category_by_id**](SnippetCategoriesApi.md#get_snippet_category_by_id) | **GET** /snippet-categories/{id} | Get a snippet category
[**list_snippet_categories**](SnippetCategoriesApi.md#list_snippet_categories) | **GET** /snippet-categories | List snippets categories


# **delete_snippet_category_by_id**
> delete_snippet_category_by_id(id)

Delete a snippet category

Delete an existing snippet category. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
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
    api_instance = scm.config_setup.SnippetCategoriesApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Delete a snippet category
        api_instance.delete_snippet_category_by_id(id)
    except Exception as e:
        print("Exception when calling SnippetCategoriesApi->delete_snippet_category_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

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

# **get_snippet_category_by_id**
> SnippetCategories get_snippet_category_by_id(id)

Get a snippet category

Retrieve an existing snippet category. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.snippet_categories import SnippetCategories
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
    api_instance = scm.config_setup.SnippetCategoriesApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get a snippet category
        api_response = api_instance.get_snippet_category_by_id(id)
        print("The response of SnippetCategoriesApi->get_snippet_category_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetCategoriesApi->get_snippet_category_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**SnippetCategories**](SnippetCategories.md)

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

# **list_snippet_categories**
> SnippetCategoriesListResponse list_snippet_categories(limit=limit, offset=offset, name=name)

List snippets categories

Retrieve a list of snippet categories. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.snippet_categories_list_response import SnippetCategoriesListResponse
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
    api_instance = scm.config_setup.SnippetCategoriesApi(api_client)
    limit = 56 # int | The maximum number of resources to return (optional)
    offset = 56 # int | The offset into the list of resources returned (optional)
    name = 'name_example' # str | The name of the resource (optional)

    try:
        # List snippets categories
        api_response = api_instance.list_snippet_categories(limit=limit, offset=offset, name=name)
        print("The response of SnippetCategoriesApi->list_snippet_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetCategoriesApi->list_snippet_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of resources to return | [optional] 
 **offset** | **int**| The offset into the list of resources returned | [optional] 
 **name** | **str**| The name of the resource | [optional] 

### Return type

[**SnippetCategoriesListResponse**](SnippetCategoriesListResponse.md)

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

