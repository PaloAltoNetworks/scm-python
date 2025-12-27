# scm.network_services.SDWANRulesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sdwan_rules**](SDWANRulesApi.md#create_sdwan_rules) | **POST** /sdwan-rules | Create an SD-WAN rule
[**delete_sdwan_rules_by_id**](SDWANRulesApi.md#delete_sdwan_rules_by_id) | **DELETE** /sdwan-rules/{id} | Delete an SD-WAN rule
[**get_sdwan_rules_by_id**](SDWANRulesApi.md#get_sdwan_rules_by_id) | **GET** /sdwan-rules/{id} | Get an SD-WAN rule
[**list_sdwan_rules**](SDWANRulesApi.md#list_sdwan_rules) | **GET** /sdwan-rules | List SD-WAN rules
[**update_sdwan_rules_by_id**](SDWANRulesApi.md#update_sdwan_rules_by_id) | **PUT** /sdwan-rules/{id} | Update an SD-WAN rule


# **create_sdwan_rules**
> SdwanRules create_sdwan_rules(sdwan_rules=sdwan_rules)

Create an SD-WAN rule

Create a new SD-WAN rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.sdwan_rules import SdwanRules
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.SDWANRulesApi(api_client)
    sdwan_rules = scm.network_services.SdwanRules() # SdwanRules | Created (optional)

    try:
        # Create an SD-WAN rule
        api_response = api_instance.create_sdwan_rules(sdwan_rules=sdwan_rules)
        print("The response of SDWANRulesApi->create_sdwan_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANRulesApi->create_sdwan_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdwan_rules** | [**SdwanRules**](SdwanRules.md)| Created | [optional] 

### Return type

[**SdwanRules**](SdwanRules.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sdwan_rules_by_id**
> delete_sdwan_rules_by_id(id)

Delete an SD-WAN rule

Delete an SD-WAN rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.SDWANRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an SD-WAN rule
        api_instance.delete_sdwan_rules_by_id(id)
    except Exception as e:
        print("Exception when calling SDWANRulesApi->delete_sdwan_rules_by_id: %s\n" % e)
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
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdwan_rules_by_id**
> SdwanRules get_sdwan_rules_by_id(id)

Get an SD-WAN rule

Get an existing SD-WAN rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.sdwan_rules import SdwanRules
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.SDWANRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an SD-WAN rule
        api_response = api_instance.get_sdwan_rules_by_id(id)
        print("The response of SDWANRulesApi->get_sdwan_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANRulesApi->get_sdwan_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**SdwanRules**](SdwanRules.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sdwan_rules**
> SDWANRulesListResponse list_sdwan_rules(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List SD-WAN rules

Retrieve a list of SD-WAN rules. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.sdwan_rules_list_response import SDWANRulesListResponse
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.SDWANRulesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List SD-WAN rules
        api_response = api_instance.list_sdwan_rules(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of SDWANRulesApi->list_sdwan_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANRulesApi->list_sdwan_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**SDWANRulesListResponse**](SDWANRulesListResponse.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sdwan_rules_by_id**
> SdwanRules update_sdwan_rules_by_id(id, sdwan_rules=sdwan_rules)

Update an SD-WAN rule

Update an existing SD-WAN rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.sdwan_rules import SdwanRules
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.SDWANRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    sdwan_rules = scm.network_services.SdwanRules() # SdwanRules | OK (optional)

    try:
        # Update an SD-WAN rule
        api_response = api_instance.update_sdwan_rules_by_id(id, sdwan_rules=sdwan_rules)
        print("The response of SDWANRulesApi->update_sdwan_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDWANRulesApi->update_sdwan_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **sdwan_rules** | [**SdwanRules**](SdwanRules.md)| OK | [optional] 

### Return type

[**SdwanRules**](SdwanRules.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

