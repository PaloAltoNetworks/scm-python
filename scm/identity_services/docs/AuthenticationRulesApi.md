# scm.identity_services.AuthenticationRulesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authentication_rules**](AuthenticationRulesApi.md#create_authentication_rules) | **POST** /authentication-rules | Create an authentication rule
[**delete_authentication_rules_by_id**](AuthenticationRulesApi.md#delete_authentication_rules_by_id) | **DELETE** /authentication-rules/{id} | Delete an authentication rule
[**get_authentication_rules_by_id**](AuthenticationRulesApi.md#get_authentication_rules_by_id) | **GET** /authentication-rules/{id} | Get an authentication rule
[**list_authentication_rules**](AuthenticationRulesApi.md#list_authentication_rules) | **GET** /authentication-rules | List authentication rules
[**move_authentication_rules_by_id**](AuthenticationRulesApi.md#move_authentication_rules_by_id) | **POST** /authentication-rules/{id}:move | Move an authentication rule
[**update_authentication_rules_by_id**](AuthenticationRulesApi.md#update_authentication_rules_by_id) | **PUT** /authentication-rules/{id} | Update an authentication rule


# **create_authentication_rules**
> AuthenticationRules create_authentication_rules(position, authentication_rules=authentication_rules)

Create an authentication rule

Create a new authentication rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.authentication_rules import AuthenticationRules
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.AuthenticationRulesApi(api_client)
    position = pre # str | The relative position of the rule  (default to pre)
    authentication_rules = scm.identity_services.AuthenticationRules() # AuthenticationRules | Created (optional)

    try:
        # Create an authentication rule
        api_response = api_instance.create_authentication_rules(position, authentication_rules=authentication_rules)
        print("The response of AuthenticationRulesApi->create_authentication_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationRulesApi->create_authentication_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The relative position of the rule  | [default to pre]
 **authentication_rules** | [**AuthenticationRules**](AuthenticationRules.md)| Created | [optional] 

### Return type

[**AuthenticationRules**](AuthenticationRules.md)

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

# **delete_authentication_rules_by_id**
> delete_authentication_rules_by_id(id)

Delete an authentication rule

Delete an authentication rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.AuthenticationRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an authentication rule
        api_instance.delete_authentication_rules_by_id(id)
    except Exception as e:
        print("Exception when calling AuthenticationRulesApi->delete_authentication_rules_by_id: %s\n" % e)
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

# **get_authentication_rules_by_id**
> AuthenticationRules get_authentication_rules_by_id(id)

Get an authentication rule

Get an existing authentication rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.authentication_rules import AuthenticationRules
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.AuthenticationRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an authentication rule
        api_response = api_instance.get_authentication_rules_by_id(id)
        print("The response of AuthenticationRulesApi->get_authentication_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationRulesApi->get_authentication_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**AuthenticationRules**](AuthenticationRules.md)

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

# **list_authentication_rules**
> AuthenticationRulesListResponse list_authentication_rules(position, name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List authentication rules

Retrieve a list of authentication rules. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.authentication_rules_list_response import AuthenticationRulesListResponse
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.AuthenticationRulesApi(api_client)
    position = pre # str | The relative position of the rule  (default to pre)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List authentication rules
        api_response = api_instance.list_authentication_rules(position, name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of AuthenticationRulesApi->list_authentication_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationRulesApi->list_authentication_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The relative position of the rule  | [default to pre]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]

### Return type

[**AuthenticationRulesListResponse**](AuthenticationRulesListResponse.md)

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

# **move_authentication_rules_by_id**
> move_authentication_rules_by_id(id, rule_based_move=rule_based_move)

Move an authentication rule

Move an existing authentication rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.rule_based_move import RuleBasedMove
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.AuthenticationRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    rule_based_move = scm.identity_services.RuleBasedMove() # RuleBasedMove | OK (optional)

    try:
        # Move an authentication rule
        api_instance.move_authentication_rules_by_id(id, rule_based_move=rule_based_move)
    except Exception as e:
        print("Exception when calling AuthenticationRulesApi->move_authentication_rules_by_id: %s\n" % e)
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

# **update_authentication_rules_by_id**
> AuthenticationRules update_authentication_rules_by_id(id, authentication_rules=authentication_rules)

Update an authentication rule

Update an existing authentication rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.authentication_rules import AuthenticationRules
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.AuthenticationRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    authentication_rules = scm.identity_services.AuthenticationRules() # AuthenticationRules | OK (optional)

    try:
        # Update an authentication rule
        api_response = api_instance.update_authentication_rules_by_id(id, authentication_rules=authentication_rules)
        print("The response of AuthenticationRulesApi->update_authentication_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationRulesApi->update_authentication_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **authentication_rules** | [**AuthenticationRules**](AuthenticationRules.md)| OK | [optional] 

### Return type

[**AuthenticationRules**](AuthenticationRules.md)

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

