# scm_config_setup.VariablesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_variable**](VariablesApi.md#create_variable) | **POST** /variables | Create a variable
[**delete_variable_by_id**](VariablesApi.md#delete_variable_by_id) | **DELETE** /variables/{id} | Delete a variable
[**get_variable_by_id**](VariablesApi.md#get_variable_by_id) | **GET** /variables/{id} | Get a variables
[**list_variables**](VariablesApi.md#list_variables) | **GET** /variables | List variables
[**update_variable_by_id**](VariablesApi.md#update_variable_by_id) | **PUT** /variables/{id} | Update a variable


# **create_variable**
> Variables create_variable(folder=folder, snippet=snippet, device=device, variables=variables)

Create a variable

Create a new variable. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.variables import Variables
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
    api_instance = scm_config_setup.VariablesApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    variables = scm_config_setup.Variables() # Variables | The `variable` resource definition. (optional)

    try:
        # Create a variable
        api_response = api_instance.create_variable(folder=folder, snippet=snippet, device=device, variables=variables)
        print("The response of VariablesApi->create_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->create_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **variables** | [**Variables**](Variables.md)| The &#x60;variable&#x60; resource definition. | [optional] 

### Return type

[**Variables**](Variables.md)

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

# **delete_variable_by_id**
> delete_variable_by_id(id)

Delete a variable

Delete an existing variable. 

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
    api_instance = scm_config_setup.VariablesApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Delete a variable
        api_instance.delete_variable_by_id(id)
    except Exception as e:
        print("Exception when calling VariablesApi->delete_variable_by_id: %s\n" % e)
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

# **get_variable_by_id**
> Variables get_variable_by_id(id)

Get a variables

Retrieve an existing variable. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.variables import Variables
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
    api_instance = scm_config_setup.VariablesApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get a variables
        api_response = api_instance.get_variable_by_id(id)
        print("The response of VariablesApi->get_variable_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->get_variable_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**Variables**](Variables.md)

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

# **list_variables**
> VariablesListResponse list_variables(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List variables

Retrieve a list of variables. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.variables_list_response import VariablesListResponse
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
    api_instance = scm_config_setup.VariablesApi(api_client)
    limit = 56 # int | The maximum number of resources to return (optional)
    offset = 56 # int | The offset into the list of resources returned (optional)
    name = 'name_example' # str | The name of the resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List variables
        api_response = api_instance.list_variables(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of VariablesApi->list_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->list_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of resources to return | [optional] 
 **offset** | **int**| The offset into the list of resources returned | [optional] 
 **name** | **str**| The name of the resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**VariablesListResponse**](VariablesListResponse.md)

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

# **update_variable_by_id**
> Variables update_variable_by_id(id, variables=variables)

Update a variable

Update an existing variable. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.variables import Variables
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
    api_instance = scm_config_setup.VariablesApi(api_client)
    id = 'id_example' # str | The UUID of the resource
    variables = scm_config_setup.Variables() # Variables | The `variable` resource definition. (optional)

    try:
        # Update a variable
        api_response = api_instance.update_variable_by_id(id, variables=variables)
        print("The response of VariablesApi->update_variable_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->update_variable_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 
 **variables** | [**Variables**](Variables.md)| The &#x60;variable&#x60; resource definition. | [optional] 

### Return type

[**Variables**](Variables.md)

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

