# scm_security_services.DoSProtectionRulesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_do_s_protection_rules**](DoSProtectionRulesApi.md#create_do_s_protection_rules) | **POST** /dos-protection-rules | Create a DoS protection rule
[**delete_do_s_protection_rules_by_id**](DoSProtectionRulesApi.md#delete_do_s_protection_rules_by_id) | **DELETE** /dos-protection-rules/{id} | Delete a DoS protection rule
[**get_do_s_protection_rules_by_id**](DoSProtectionRulesApi.md#get_do_s_protection_rules_by_id) | **GET** /dos-protection-rules/{id} | Get a DoS protection rule
[**list_do_s_protection_rules**](DoSProtectionRulesApi.md#list_do_s_protection_rules) | **GET** /dos-protection-rules | List DoS protection rules
[**update_do_s_protection_rules_by_id**](DoSProtectionRulesApi.md#update_do_s_protection_rules_by_id) | **PUT** /dos-protection-rules/{id} | Update a DoS protection rule


# **create_do_s_protection_rules**
> DosProtectionRules create_do_s_protection_rules(dos_protection_rules=dos_protection_rules)

Create a DoS protection rule

Create a new DoS protection rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.dos_protection_rules import DosProtectionRules
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
    api_instance = scm_security_services.DoSProtectionRulesApi(api_client)
    dos_protection_rules = scm_security_services.DosProtectionRules() # DosProtectionRules | Created (optional)

    try:
        # Create a DoS protection rule
        api_response = api_instance.create_do_s_protection_rules(dos_protection_rules=dos_protection_rules)
        print("The response of DoSProtectionRulesApi->create_do_s_protection_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoSProtectionRulesApi->create_do_s_protection_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dos_protection_rules** | [**DosProtectionRules**](DosProtectionRules.md)| Created | [optional] 

### Return type

[**DosProtectionRules**](DosProtectionRules.md)

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

# **delete_do_s_protection_rules_by_id**
> delete_do_s_protection_rules_by_id(id)

Delete a DoS protection rule

Delete a DoS protection rule. 

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
    api_instance = scm_security_services.DoSProtectionRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a DoS protection rule
        api_instance.delete_do_s_protection_rules_by_id(id)
    except Exception as e:
        print("Exception when calling DoSProtectionRulesApi->delete_do_s_protection_rules_by_id: %s\n" % e)
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

# **get_do_s_protection_rules_by_id**
> DosProtectionRules get_do_s_protection_rules_by_id(id)

Get a DoS protection rule

Get an existing DoS protection rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.dos_protection_rules import DosProtectionRules
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
    api_instance = scm_security_services.DoSProtectionRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a DoS protection rule
        api_response = api_instance.get_do_s_protection_rules_by_id(id)
        print("The response of DoSProtectionRulesApi->get_do_s_protection_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoSProtectionRulesApi->get_do_s_protection_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**DosProtectionRules**](DosProtectionRules.md)

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

# **list_do_s_protection_rules**
> DoSProtectionRulesListResponse list_do_s_protection_rules(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List DoS protection rules

Retrieve a list of DoS protection rules. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.do_s_protection_rules_list_response import DoSProtectionRulesListResponse
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
    api_instance = scm_security_services.DoSProtectionRulesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List DoS protection rules
        api_response = api_instance.list_do_s_protection_rules(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of DoSProtectionRulesApi->list_do_s_protection_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoSProtectionRulesApi->list_do_s_protection_rules: %s\n" % e)
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

[**DoSProtectionRulesListResponse**](DoSProtectionRulesListResponse.md)

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

# **update_do_s_protection_rules_by_id**
> DosProtectionRules update_do_s_protection_rules_by_id(id, dos_protection_rules=dos_protection_rules)

Update a DoS protection rule

Update an existing DoS protection rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.dos_protection_rules import DosProtectionRules
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
    api_instance = scm_security_services.DoSProtectionRulesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    dos_protection_rules = scm_security_services.DosProtectionRules() # DosProtectionRules | OK (optional)

    try:
        # Update a DoS protection rule
        api_response = api_instance.update_do_s_protection_rules_by_id(id, dos_protection_rules=dos_protection_rules)
        print("The response of DoSProtectionRulesApi->update_do_s_protection_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoSProtectionRulesApi->update_do_s_protection_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **dos_protection_rules** | [**DosProtectionRules**](DosProtectionRules.md)| OK | [optional] 

### Return type

[**DosProtectionRules**](DosProtectionRules.md)

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

