# scm_security_services.ApplicationOverrideRulesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_override_rules**](ApplicationOverrideRulesApi.md#create_application_override_rules) | **POST** /app-override-rules | Create an application override rule
[**delete_application_override_rules_by_id**](ApplicationOverrideRulesApi.md#delete_application_override_rules_by_id) | **DELETE** /app-override-rules/{id} | Delete an application override rule
[**get_application_override_rules_by_id**](ApplicationOverrideRulesApi.md#get_application_override_rules_by_id) | **GET** /app-override-rules/{id} | Get an application override rule
[**list_application_override_rules**](ApplicationOverrideRulesApi.md#list_application_override_rules) | **GET** /app-override-rules | List application override rules
[**move_application_override_rules_by_id**](ApplicationOverrideRulesApi.md#move_application_override_rules_by_id) | **POST** /app-override-rules/{id}:move | Move an application override rule
[**update_application_override_rules_by_id**](ApplicationOverrideRulesApi.md#update_application_override_rules_by_id) | **PUT** /app-override-rules/{id} | Update an application override rule


# **create_application_override_rules**
> AppOverrideRules create_application_override_rules(position, app_override_rules=app_override_rules)

Create an application override rule

Create a new application override rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.app_override_rules import AppOverrideRules
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
    api_instance = scm_security_services.ApplicationOverrideRulesApi(api_client)
    position = pre # str | The position of a security rule  (default to pre)
    app_override_rules = scm_security_services.AppOverrideRules() # AppOverrideRules | Created (optional)

    try:
        # Create an application override rule
        api_response = api_instance.create_application_override_rules(position, app_override_rules=app_override_rules)
        print("The response of ApplicationOverrideRulesApi->create_application_override_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationOverrideRulesApi->create_application_override_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The position of a security rule  | [default to pre]
 **app_override_rules** | [**AppOverrideRules**](AppOverrideRules.md)| Created | [optional] 

### Return type

[**AppOverrideRules**](AppOverrideRules.md)

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

# **delete_application_override_rules_by_id**
> delete_application_override_rules_by_id(id)

Delete an application override rule

Delete an application override rule. 

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
    api_instance = scm_security_services.ApplicationOverrideRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an application override rule
        api_instance.delete_application_override_rules_by_id(id)
    except Exception as e:
        print("Exception when calling ApplicationOverrideRulesApi->delete_application_override_rules_by_id: %s\n" % e)
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

# **get_application_override_rules_by_id**
> AppOverrideRules get_application_override_rules_by_id(id)

Get an application override rule

Get an existing application override rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.app_override_rules import AppOverrideRules
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
    api_instance = scm_security_services.ApplicationOverrideRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an application override rule
        api_response = api_instance.get_application_override_rules_by_id(id)
        print("The response of ApplicationOverrideRulesApi->get_application_override_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationOverrideRulesApi->get_application_override_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**AppOverrideRules**](AppOverrideRules.md)

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

# **list_application_override_rules**
> ApplicationOverrideRulesListResponse list_application_override_rules(position, name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List application override rules

Retrieve a list of application override rules. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.application_override_rules_list_response import ApplicationOverrideRulesListResponse
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
    api_instance = scm_security_services.ApplicationOverrideRulesApi(api_client)
    position = pre # str | The position of a security rule  (default to pre)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List application override rules
        api_response = api_instance.list_application_override_rules(position, name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of ApplicationOverrideRulesApi->list_application_override_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationOverrideRulesApi->list_application_override_rules: %s\n" % e)
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

[**ApplicationOverrideRulesListResponse**](ApplicationOverrideRulesListResponse.md)

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

# **move_application_override_rules_by_id**
> move_application_override_rules_by_id(id, rule_based_move=rule_based_move)

Move an application override rule

Move an existing application override rule. 

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
    api_instance = scm_security_services.ApplicationOverrideRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    rule_based_move = scm_security_services.RuleBasedMove() # RuleBasedMove | The app override rule you want to move (optional)

    try:
        # Move an application override rule
        api_instance.move_application_override_rules_by_id(id, rule_based_move=rule_based_move)
    except Exception as e:
        print("Exception when calling ApplicationOverrideRulesApi->move_application_override_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **rule_based_move** | [**RuleBasedMove**](RuleBasedMove.md)| The app override rule you want to move | [optional] 

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

# **update_application_override_rules_by_id**
> AppOverrideRules update_application_override_rules_by_id(id, app_override_rules=app_override_rules)

Update an application override rule

Update an existing application override rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.app_override_rules import AppOverrideRules
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
    api_instance = scm_security_services.ApplicationOverrideRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    app_override_rules = scm_security_services.AppOverrideRules() # AppOverrideRules | OK (optional)

    try:
        # Update an application override rule
        api_response = api_instance.update_application_override_rules_by_id(id, app_override_rules=app_override_rules)
        print("The response of ApplicationOverrideRulesApi->update_application_override_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationOverrideRulesApi->update_application_override_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **app_override_rules** | [**AppOverrideRules**](AppOverrideRules.md)| OK | [optional] 

### Return type

[**AppOverrideRules**](AppOverrideRules.md)

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

