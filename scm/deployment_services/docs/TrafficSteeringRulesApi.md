# scm.deployment_services.TrafficSteeringRulesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_traffic_steering_rules**](TrafficSteeringRulesApi.md#create_traffic_steering_rules) | **POST** /traffic-steering-rules | Create a traffic steering rule
[**delete_traffic_steering_rules_by_id**](TrafficSteeringRulesApi.md#delete_traffic_steering_rules_by_id) | **DELETE** /traffic-steering-rules/{id} | Delete a traffic steering rule
[**get_traffic_steering_rules_by_id**](TrafficSteeringRulesApi.md#get_traffic_steering_rules_by_id) | **GET** /traffic-steering-rules/{id} | Get a traffic steering rule
[**list_traffic_steering_rules**](TrafficSteeringRulesApi.md#list_traffic_steering_rules) | **GET** /traffic-steering-rules | List traffic steering rules
[**update_traffic_steering_rules_by_id**](TrafficSteeringRulesApi.md#update_traffic_steering_rules_by_id) | **PUT** /traffic-steering-rules/{id} | Update a traffic steering rule


# **create_traffic_steering_rules**
> TrafficSteeringRules create_traffic_steering_rules(folder, traffic_steering_rules=traffic_steering_rules)

Create a traffic steering rule

Create a new Service Connection traffic steering rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.traffic_steering_rules import TrafficSteeringRules
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.TrafficSteeringRulesApi(api_client)
    folder = Service Connections # str | The folder in which the resource is defined  (default to Service Connections)
    traffic_steering_rules = scm.deployment_services.TrafficSteeringRules() # TrafficSteeringRules | Created (optional)

    try:
        # Create a traffic steering rule
        api_response = api_instance.create_traffic_steering_rules(folder, traffic_steering_rules=traffic_steering_rules)
        print("The response of TrafficSteeringRulesApi->create_traffic_steering_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficSteeringRulesApi->create_traffic_steering_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [default to Service Connections]
 **traffic_steering_rules** | [**TrafficSteeringRules**](TrafficSteeringRules.md)| Created | [optional] 

### Return type

[**TrafficSteeringRules**](TrafficSteeringRules.md)

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

# **delete_traffic_steering_rules_by_id**
> delete_traffic_steering_rules_by_id(id)

Delete a traffic steering rule

Delete a Service Connection traffic steering rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.TrafficSteeringRulesApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Delete a traffic steering rule
        api_instance.delete_traffic_steering_rules_by_id(id)
    except Exception as e:
        print("Exception when calling TrafficSteeringRulesApi->delete_traffic_steering_rules_by_id: %s\n" % e)
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

# **get_traffic_steering_rules_by_id**
> TrafficSteeringRules get_traffic_steering_rules_by_id(id)

Get a traffic steering rule

Get an existing Service Connection traffic steering rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.traffic_steering_rules import TrafficSteeringRules
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.TrafficSteeringRulesApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Get a traffic steering rule
        api_response = api_instance.get_traffic_steering_rules_by_id(id)
        print("The response of TrafficSteeringRulesApi->get_traffic_steering_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficSteeringRulesApi->get_traffic_steering_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**TrafficSteeringRules**](TrafficSteeringRules.md)

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

# **list_traffic_steering_rules**
> TrafficSteeringRulesListResponse list_traffic_steering_rules(folder, name=name, limit=limit, offset=offset)

List traffic steering rules

Retrieve a list of Service Connection traffic steering rules. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.traffic_steering_rules_list_response import TrafficSteeringRulesListResponse
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.TrafficSteeringRulesApi(api_client)
    folder = Service Connections # str | The folder in which the resource is defined  (default to Service Connections)
    name = 'name_example' # str | The name of the configuration resource (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List traffic steering rules
        api_response = api_instance.list_traffic_steering_rules(folder, name=name, limit=limit, offset=offset)
        print("The response of TrafficSteeringRulesApi->list_traffic_steering_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficSteeringRulesApi->list_traffic_steering_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [default to Service Connections]
 **name** | **str**| The name of the configuration resource | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]

### Return type

[**TrafficSteeringRulesListResponse**](TrafficSteeringRulesListResponse.md)

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

# **update_traffic_steering_rules_by_id**
> TrafficSteeringRules update_traffic_steering_rules_by_id(id, traffic_steering_rules=traffic_steering_rules)

Update a traffic steering rule

Update an existing Service Connection traffic steering rule. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.traffic_steering_rules import TrafficSteeringRules
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.TrafficSteeringRulesApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource
    traffic_steering_rules = scm.deployment_services.TrafficSteeringRules() # TrafficSteeringRules | OK (optional)

    try:
        # Update a traffic steering rule
        api_response = api_instance.update_traffic_steering_rules_by_id(id, traffic_steering_rules=traffic_steering_rules)
        print("The response of TrafficSteeringRulesApi->update_traffic_steering_rules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficSteeringRulesApi->update_traffic_steering_rules_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **traffic_steering_rules** | [**TrafficSteeringRules**](TrafficSteeringRules.md)| OK | [optional] 

### Return type

[**TrafficSteeringRules**](TrafficSteeringRules.md)

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

