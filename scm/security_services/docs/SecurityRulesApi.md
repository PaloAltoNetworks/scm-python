# scm.security_services.SecurityRulesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_security_rules**](SecurityRulesApi.md#create_security_rules) | **POST** /security-rules | Create a security rule
[**delete_security_rules_by_id**](SecurityRulesApi.md#delete_security_rules_by_id) | **DELETE** /security-rules/{id} | Delete a security rule
[**get_security_rules_by_id**](SecurityRulesApi.md#get_security_rules_by_id) | **GET** /security-rules/{id} | Get a security rule
[**list_rules**](SecurityRulesApi.md#list_rules) | **GET** /security-rules | List security rules
[**move_security_rules_by_id**](SecurityRulesApi.md#move_security_rules_by_id) | **POST** /security-rules/{id}:move | Move a security rule
[**update_security_rules_by_id**](SecurityRulesApi.md#update_security_rules_by_id) | **PUT** /security-rules/{id} | Update a security rule


# **create_security_rules**
> SecurityRules create_security_rules(position, security_rules=security_rules)

Create a security rule

Create a new security rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.security_rules import SecurityRules
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
    api_instance = scm.security_services.SecurityRulesApi(api_client)
    position = pre # str | The position of a security rule  (default to pre)
    security_rules = scm.security_services.SecurityRules() # SecurityRules | Created (optional)

    try:
        # Create a security rule
        api_response = api_instance.create_security_rules(position, security_rules=security_rules)
        print("The response of SecurityRulesApi->create_security_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityRulesApi->create_security_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The position of a security rule  | [default to pre]
 **security_rules** | [**SecurityRules**](SecurityRules.md)| Created | [optional] 

### Return type

[**SecurityRules**](SecurityRules.md)

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

# **delete_security_rules_by_id**
> delete_security_rules_by_id(id)

Delete a security rule

Delete a security rule. 

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
    api_instance = scm.security_services.SecurityRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a security rule
        api_instance.delete_security_rules_by_id(id)
    except Exception as e:
        print("Exception when calling SecurityRulesApi->delete_security_rules_by_id: %s\n" % e)
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

# **get_security_rules_by_id**
> SecurityRules get_security_rules_by_id(id)

Get a security rule

Get an existing security rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.security_rules import SecurityRules
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
    api_instance = scm.security_services.SecurityRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a security rule
        api_response = api_instance.get_security_rules_by_id(id)
        print("The response of SecurityRulesApi->get_security_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityRulesApi->get_security_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**SecurityRules**](SecurityRules.md)

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

# **list_rules**
> RulesListResponse list_rules(position, name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List security rules

Retrieve a list of security rules. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.rules_list_response import RulesListResponse
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
    api_instance = scm.security_services.SecurityRulesApi(api_client)
    position = pre # str | The position of a security rule  (default to pre)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List security rules
        api_response = api_instance.list_rules(position, name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of SecurityRulesApi->list_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityRulesApi->list_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The position of a security rule  | [default to pre]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]

### Return type

[**RulesListResponse**](RulesListResponse.md)

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

# **move_security_rules_by_id**
> move_security_rules_by_id(id, rule_based_move=rule_based_move)

Move a security rule

Move an existing security rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.rule_based_move import RuleBasedMove
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
    api_instance = scm.security_services.SecurityRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    rule_based_move = scm.security_services.RuleBasedMove() # RuleBasedMove | OK (optional)

    try:
        # Move a security rule
        api_instance.move_security_rules_by_id(id, rule_based_move=rule_based_move)
    except Exception as e:
        print("Exception when calling SecurityRulesApi->move_security_rules_by_id: %s\n" % e)
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_security_rules_by_id**
> SecurityRules update_security_rules_by_id(id, security_rules=security_rules)

Update a security rule

Update an existing security rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.security_rules import SecurityRules
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
    api_instance = scm.security_services.SecurityRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    security_rules = scm.security_services.SecurityRules() # SecurityRules | OK (optional)

    try:
        # Update a security rule
        api_response = api_instance.update_security_rules_by_id(id, security_rules=security_rules)
        print("The response of SecurityRulesApi->update_security_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityRulesApi->update_security_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **security_rules** | [**SecurityRules**](SecurityRules.md)| OK | [optional] 

### Return type

[**SecurityRules**](SecurityRules.md)

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

