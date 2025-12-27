# scm_network_services.QoSRulesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_qo_s_policy_rules**](QoSRulesApi.md#create_qo_s_policy_rules) | **POST** /qos-policy-rules | Create a QoS policy rule
[**delete_qo_s_policy_rules_by_id**](QoSRulesApi.md#delete_qo_s_policy_rules_by_id) | **DELETE** /qos-policy-rules/{id} | Delete a QoS policy rule
[**get_qo_s_policy_rules_by_id**](QoSRulesApi.md#get_qo_s_policy_rules_by_id) | **GET** /qos-policy-rules/{id} | Get a QoS policy rule
[**list_qo_s_policy_rules**](QoSRulesApi.md#list_qo_s_policy_rules) | **GET** /qos-policy-rules | List QoS policy rules
[**move_qo_s_policy_rules_by_id**](QoSRulesApi.md#move_qo_s_policy_rules_by_id) | **POST** /qos-policy-rules/{id}:move | Move a QoS policy rule
[**update_qo_s_policy_rules_by_id**](QoSRulesApi.md#update_qo_s_policy_rules_by_id) | **PUT** /qos-policy-rules/{id} | Update a QoS policy rule


# **create_qo_s_policy_rules**
> QosPolicyRules create_qo_s_policy_rules(position, qos_policy_rules=qos_policy_rules)

Create a QoS policy rule

Create a new QoS policy rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.qos_policy_rules import QosPolicyRules
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.QoSRulesApi(api_client)
    position = pre # str | The relative position of the rule (default to pre)
    qos_policy_rules = scm_network_services.QosPolicyRules() # QosPolicyRules | Created (optional)

    try:
        # Create a QoS policy rule
        api_response = api_instance.create_qo_s_policy_rules(position, qos_policy_rules=qos_policy_rules)
        print("The response of QoSRulesApi->create_qo_s_policy_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QoSRulesApi->create_qo_s_policy_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The relative position of the rule | [default to pre]
 **qos_policy_rules** | [**QosPolicyRules**](QosPolicyRules.md)| Created | [optional] 

### Return type

[**QosPolicyRules**](QosPolicyRules.md)

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

# **delete_qo_s_policy_rules_by_id**
> delete_qo_s_policy_rules_by_id(id)

Delete a QoS policy rule

Delete a Qos policy rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.QoSRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a QoS policy rule
        api_instance.delete_qo_s_policy_rules_by_id(id)
    except Exception as e:
        print("Exception when calling QoSRulesApi->delete_qo_s_policy_rules_by_id: %s\n" % e)
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

# **get_qo_s_policy_rules_by_id**
> QosPolicyRules get_qo_s_policy_rules_by_id(id)

Get a QoS policy rule

Get an existing QoS policy rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.qos_policy_rules import QosPolicyRules
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.QoSRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a QoS policy rule
        api_response = api_instance.get_qo_s_policy_rules_by_id(id)
        print("The response of QoSRulesApi->get_qo_s_policy_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QoSRulesApi->get_qo_s_policy_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**QosPolicyRules**](QosPolicyRules.md)

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

# **list_qo_s_policy_rules**
> QoSPolicyRulesListResponse list_qo_s_policy_rules(position, name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List QoS policy rules

Retrieve a list of QoS policy rules. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.qo_s_policy_rules_list_response import QoSPolicyRulesListResponse
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.QoSRulesApi(api_client)
    position = pre # str | The relative position of the rule (default to pre)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List QoS policy rules
        api_response = api_instance.list_qo_s_policy_rules(position, name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of QoSRulesApi->list_qo_s_policy_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QoSRulesApi->list_qo_s_policy_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The relative position of the rule | [default to pre]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]

### Return type

[**QoSPolicyRulesListResponse**](QoSPolicyRulesListResponse.md)

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

# **move_qo_s_policy_rules_by_id**
> move_qo_s_policy_rules_by_id(id, rule_based_move=rule_based_move)

Move a QoS policy rule

Move a QoS policy rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.rule_based_move import RuleBasedMove
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.QoSRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    rule_based_move = scm_network_services.RuleBasedMove() # RuleBasedMove | OK (optional)

    try:
        # Move a QoS policy rule
        api_instance.move_qo_s_policy_rules_by_id(id, rule_based_move=rule_based_move)
    except Exception as e:
        print("Exception when calling QoSRulesApi->move_qo_s_policy_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **rule_based_move** | [**RuleBasedMove**](RuleBasedMove.md)| OK | [optional] 

### Return type

void (empty response body)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_qo_s_policy_rules_by_id**
> QosPolicyRules update_qo_s_policy_rules_by_id(id, qos_policy_rules=qos_policy_rules)

Update a QoS policy rule

Update an existing QoS policy rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.qos_policy_rules import QosPolicyRules
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.QoSRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    qos_policy_rules = scm_network_services.QosPolicyRules() # QosPolicyRules | OK (optional)

    try:
        # Update a QoS policy rule
        api_response = api_instance.update_qo_s_policy_rules_by_id(id, qos_policy_rules=qos_policy_rules)
        print("The response of QoSRulesApi->update_qo_s_policy_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QoSRulesApi->update_qo_s_policy_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **qos_policy_rules** | [**QosPolicyRules**](QosPolicyRules.md)| OK | [optional] 

### Return type

[**QosPolicyRules**](QosPolicyRules.md)

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

