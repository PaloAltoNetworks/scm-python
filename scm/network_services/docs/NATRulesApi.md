# scm.network_services.NATRulesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nat_rules**](NATRulesApi.md#create_nat_rules) | **POST** /nat-rules | Create a NAT rule
[**delete_nat_rules_by_id**](NATRulesApi.md#delete_nat_rules_by_id) | **DELETE** /nat-rules/{id} | Delete a NAT rule
[**get_nat_rules_by_id**](NATRulesApi.md#get_nat_rules_by_id) | **GET** /nat-rules/{id} | Get a NAT rule
[**list_nat_rules**](NATRulesApi.md#list_nat_rules) | **GET** /nat-rules | List NAT rules
[**update_nat_rules_by_id**](NATRulesApi.md#update_nat_rules_by_id) | **PUT** /nat-rules/{id} | Update a NAT rule


# **create_nat_rules**
> NatRules create_nat_rules(position, nat_rules=nat_rules)

Create a NAT rule

Create a new NAT rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.nat_rules import NatRules
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
    api_instance = scm.network_services.NATRulesApi(api_client)
    position = pre # str | The relative position of the rule (default to pre)
    nat_rules = scm.network_services.NatRules() # NatRules | Created (optional)

    try:
        # Create a NAT rule
        api_response = api_instance.create_nat_rules(position, nat_rules=nat_rules)
        print("The response of NATRulesApi->create_nat_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NATRulesApi->create_nat_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The relative position of the rule | [default to pre]
 **nat_rules** | [**NatRules**](NatRules.md)| Created | [optional] 

### Return type

[**NatRules**](NatRules.md)

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

# **delete_nat_rules_by_id**
> delete_nat_rules_by_id(id)

Delete a NAT rule

Delete a NAT rule. 

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
    api_instance = scm.network_services.NATRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a NAT rule
        api_instance.delete_nat_rules_by_id(id)
    except Exception as e:
        print("Exception when calling NATRulesApi->delete_nat_rules_by_id: %s\n" % e)
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

# **get_nat_rules_by_id**
> NatRules get_nat_rules_by_id(id)

Get a NAT rule

Get an existing NAT rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.nat_rules import NatRules
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
    api_instance = scm.network_services.NATRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a NAT rule
        api_response = api_instance.get_nat_rules_by_id(id)
        print("The response of NATRulesApi->get_nat_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NATRulesApi->get_nat_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**NatRules**](NatRules.md)

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

# **list_nat_rules**
> NatRulesListResponse list_nat_rules(position, limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List NAT rules

Retrieve a list of NAT rules. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.nat_rules_list_response import NatRulesListResponse
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
    api_instance = scm.network_services.NATRulesApi(api_client)
    position = pre # str | The relative position of the rule (default to pre)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List NAT rules
        api_response = api_instance.list_nat_rules(position, limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of NATRulesApi->list_nat_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NATRulesApi->list_nat_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The relative position of the rule | [default to pre]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**NatRulesListResponse**](NatRulesListResponse.md)

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

# **update_nat_rules_by_id**
> NatRules update_nat_rules_by_id(id, position, nat_rules=nat_rules)

Update a NAT rule

Update an existing NAT rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.nat_rules import NatRules
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
    api_instance = scm.network_services.NATRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    position = pre # str | The relative position of the rule (default to pre)
    nat_rules = scm.network_services.NatRules() # NatRules | OK (optional)

    try:
        # Update a NAT rule
        api_response = api_instance.update_nat_rules_by_id(id, position, nat_rules=nat_rules)
        print("The response of NATRulesApi->update_nat_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NATRulesApi->update_nat_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **position** | **str**| The relative position of the rule | [default to pre]
 **nat_rules** | [**NatRules**](NatRules.md)| OK | [optional] 

### Return type

[**NatRules**](NatRules.md)

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

