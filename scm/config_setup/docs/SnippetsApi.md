# scm_config_setup.SnippetsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snippet**](SnippetsApi.md#create_snippet) | **POST** /snippets | Create a snippet
[**delete_snippet_by_id**](SnippetsApi.md#delete_snippet_by_id) | **DELETE** /snippets/{id} | Delete a snippet
[**get_snippet_by_id**](SnippetsApi.md#get_snippet_by_id) | **GET** /snippets/{id} | Get a snippet
[**list_snippets**](SnippetsApi.md#list_snippets) | **GET** /snippets | List snippets
[**update_snippet_by_id**](SnippetsApi.md#update_snippet_by_id) | **PUT** /snippets/{id} | Update a snippet


# **create_snippet**
> Snippets create_snippet(snippets=snippets)

Create a snippet

Create a new snippet. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.snippets import Snippets
from scm_config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_config_setup.SnippetsApi(api_client)
    snippets = scm_config_setup.Snippets() # Snippets | The `snippet` resource definition. (optional)

    try:
        # Create a snippet
        api_response = api_instance.create_snippet(snippets=snippets)
        print("The response of SnippetsApi->create_snippet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetsApi->create_snippet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippets** | [**Snippets**](Snippets.md)| The &#x60;snippet&#x60; resource definition. | [optional] 

### Return type

[**Snippets**](Snippets.md)

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

# **delete_snippet_by_id**
> delete_snippet_by_id(id)

Delete a snippet

Delete an existing snippet. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_config_setup.SnippetsApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Delete a snippet
        api_instance.delete_snippet_by_id(id)
    except Exception as e:
        print("Exception when calling SnippetsApi->delete_snippet_by_id: %s\n" % e)
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

# **get_snippet_by_id**
> Snippets get_snippet_by_id(id)

Get a snippet

Retrieve an existing snippet. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.snippets import Snippets
from scm_config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_config_setup.SnippetsApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get a snippet
        api_response = api_instance.get_snippet_by_id(id)
        print("The response of SnippetsApi->get_snippet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetsApi->get_snippet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**Snippets**](Snippets.md)

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

# **list_snippets**
> SnippetsListResponse list_snippets(limit=limit, offset=offset, name=name)

List snippets

Retrieve a list of snippets. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.snippets_list_response import SnippetsListResponse
from scm_config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_config_setup.SnippetsApi(api_client)
    limit = 56 # int | The maximum number of resources to return (optional)
    offset = 56 # int | The offset into the list of resources returned (optional)
    name = 'name_example' # str | The name of the resource (optional)

    try:
        # List snippets
        api_response = api_instance.list_snippets(limit=limit, offset=offset, name=name)
        print("The response of SnippetsApi->list_snippets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetsApi->list_snippets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of resources to return | [optional] 
 **offset** | **int**| The offset into the list of resources returned | [optional] 
 **name** | **str**| The name of the resource | [optional] 

### Return type

[**SnippetsListResponse**](SnippetsListResponse.md)

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

# **update_snippet_by_id**
> Snippets update_snippet_by_id(id, snippets=snippets)

Update a snippet

Update an existing snippet. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.snippets import Snippets
from scm_config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_config_setup.SnippetsApi(api_client)
    id = 'id_example' # str | The UUID of the resource
    snippets = scm_config_setup.Snippets() # Snippets | The `snippet` resource definition. (optional)

    try:
        # Update a snippet
        api_response = api_instance.update_snippet_by_id(id, snippets=snippets)
        print("The response of SnippetsApi->update_snippet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetsApi->update_snippet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 
 **snippets** | [**Snippets**](Snippets.md)| The &#x60;snippet&#x60; resource definition. | [optional] 

### Return type

[**Snippets**](Snippets.md)

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

