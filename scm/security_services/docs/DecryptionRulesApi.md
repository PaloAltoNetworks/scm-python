# scm_security_services.DecryptionRulesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_decryption_rules**](DecryptionRulesApi.md#create_decryption_rules) | **POST** /decryption-rules | Create a decryption rule
[**delete_decryption_rules_by_id**](DecryptionRulesApi.md#delete_decryption_rules_by_id) | **DELETE** /decryption-rules/{id} | Delete a decryption rule
[**get_decryption_rules_by_id**](DecryptionRulesApi.md#get_decryption_rules_by_id) | **GET** /decryption-rules/{id} | Get a decryption rule
[**list_decryption_rules**](DecryptionRulesApi.md#list_decryption_rules) | **GET** /decryption-rules | List decryption rules
[**move_decryption_rules_by_id**](DecryptionRulesApi.md#move_decryption_rules_by_id) | **POST** /decryption-rules/{id}:move | Move a decryption rule
[**update_decryption_rules_by_id**](DecryptionRulesApi.md#update_decryption_rules_by_id) | **PUT** /decryption-rules/{id} | Update a decryption rule


# **create_decryption_rules**
> DecryptionRules create_decryption_rules(position, decryption_rules=decryption_rules)

Create a decryption rule

Create a new decryption rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.decryption_rules import DecryptionRules
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionRulesApi(api_client)
    position = pre # str | The position of a security rule  (default to pre)
    decryption_rules = scm_security_services.DecryptionRules() # DecryptionRules | Created (optional)

    try:
        # Create a decryption rule
        api_response = api_instance.create_decryption_rules(position, decryption_rules=decryption_rules)
        print("The response of DecryptionRulesApi->create_decryption_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecryptionRulesApi->create_decryption_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The position of a security rule  | [default to pre]
 **decryption_rules** | [**DecryptionRules**](DecryptionRules.md)| Created | [optional] 

### Return type

[**DecryptionRules**](DecryptionRules.md)

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

# **delete_decryption_rules_by_id**
> delete_decryption_rules_by_id(id)

Delete a decryption rule

Delete a decryption rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a decryption rule
        api_instance.delete_decryption_rules_by_id(id)
    except Exception as e:
        print("Exception when calling DecryptionRulesApi->delete_decryption_rules_by_id: %s\n" % e)
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

# **get_decryption_rules_by_id**
> DecryptionRules get_decryption_rules_by_id(id)

Get a decryption rule

Get an existing decryption rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.decryption_rules import DecryptionRules
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a decryption rule
        api_response = api_instance.get_decryption_rules_by_id(id)
        print("The response of DecryptionRulesApi->get_decryption_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecryptionRulesApi->get_decryption_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**DecryptionRules**](DecryptionRules.md)

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

# **list_decryption_rules**
> DecryptionRulesListResponse list_decryption_rules(position, name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List decryption rules

Retrieve a list of decryption rules. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.decryption_rules_list_response import DecryptionRulesListResponse
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionRulesApi(api_client)
    position = pre # str | The position of a security rule  (default to pre)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List decryption rules
        api_response = api_instance.list_decryption_rules(position, name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of DecryptionRulesApi->list_decryption_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecryptionRulesApi->list_decryption_rules: %s\n" % e)
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

[**DecryptionRulesListResponse**](DecryptionRulesListResponse.md)

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

# **move_decryption_rules_by_id**
> move_decryption_rules_by_id(id, rule_based_move=rule_based_move)

Move a decryption rule

Move an existing decryption rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.rule_based_move import RuleBasedMove
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    rule_based_move = scm_security_services.RuleBasedMove() # RuleBasedMove | OK (optional)

    try:
        # Move a decryption rule
        api_instance.move_decryption_rules_by_id(id, rule_based_move=rule_based_move)
    except Exception as e:
        print("Exception when calling DecryptionRulesApi->move_decryption_rules_by_id: %s\n" % e)
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

# **update_decryption_rules_by_id**
> DecryptionRules update_decryption_rules_by_id(id, decryption_rules=decryption_rules)

Update a decryption rule

Update an existing decryption rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.decryption_rules import DecryptionRules
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    decryption_rules = scm_security_services.DecryptionRules() # DecryptionRules | OK (optional)

    try:
        # Update a decryption rule
        api_response = api_instance.update_decryption_rules_by_id(id, decryption_rules=decryption_rules)
        print("The response of DecryptionRulesApi->update_decryption_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecryptionRulesApi->update_decryption_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **decryption_rules** | [**DecryptionRules**](DecryptionRules.md)| OK | [optional] 

### Return type

[**DecryptionRules**](DecryptionRules.md)

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

