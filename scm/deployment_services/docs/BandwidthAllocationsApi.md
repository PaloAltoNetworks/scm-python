# scm_deployment_services.BandwidthAllocationsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bandwidth_allocations**](BandwidthAllocationsApi.md#create_bandwidth_allocations) | **POST** /bandwidth-allocations | Create a bandwidth allocation
[**delete_bandwidth_allocations**](BandwidthAllocationsApi.md#delete_bandwidth_allocations) | **DELETE** /bandwidth-allocations | Delete a bandwidth allocation
[**list_bandwidth_allocations**](BandwidthAllocationsApi.md#list_bandwidth_allocations) | **GET** /bandwidth-allocations | List bandwidth regions
[**update_bandwidth_allocations**](BandwidthAllocationsApi.md#update_bandwidth_allocations) | **PUT** /bandwidth-allocations | Update a bandwidth allocation


# **create_bandwidth_allocations**
> BandwidthAllocations create_bandwidth_allocations(bandwidth_allocations=bandwidth_allocations)

Create a bandwidth allocation

Create a new bandwidth allocation. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.bandwidth_allocations import BandwidthAllocations
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.BandwidthAllocationsApi(api_client)
    bandwidth_allocations = scm_deployment_services.BandwidthAllocations() # BandwidthAllocations | The `bandwidth-allocations` resource definition. (optional)

    try:
        # Create a bandwidth allocation
        api_response = api_instance.create_bandwidth_allocations(bandwidth_allocations=bandwidth_allocations)
        print("The response of BandwidthAllocationsApi->create_bandwidth_allocations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthAllocationsApi->create_bandwidth_allocations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bandwidth_allocations** | [**BandwidthAllocations**](BandwidthAllocations.md)| The &#x60;bandwidth-allocations&#x60; resource definition. | [optional] 

### Return type

[**BandwidthAllocations**](BandwidthAllocations.md)

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

# **delete_bandwidth_allocations**
> delete_bandwidth_allocations(name, spn_name_list)

Delete a bandwidth allocation

Delete a bandwidth allocation. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.BandwidthAllocationsApi(api_client)
    name = 'name_example' # str | The name of the aggregated bandwidth region
    spn_name_list = 'spn_name_list_example' # str | Comma separated of the spn_name_list name per region

    try:
        # Delete a bandwidth allocation
        api_instance.delete_bandwidth_allocations(name, spn_name_list)
    except Exception as e:
        print("Exception when calling BandwidthAllocationsApi->delete_bandwidth_allocations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the aggregated bandwidth region | 
 **spn_name_list** | **str**| Comma separated of the spn_name_list name per region | 

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

# **list_bandwidth_allocations**
> BandwidthAllocationsListResponse list_bandwidth_allocations(limit=limit, offset=offset)

List bandwidth regions

Retrieve a list of bandwidth regions. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.bandwidth_allocations_list_response import BandwidthAllocationsListResponse
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.BandwidthAllocationsApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List bandwidth regions
        api_response = api_instance.list_bandwidth_allocations(limit=limit, offset=offset)
        print("The response of BandwidthAllocationsApi->list_bandwidth_allocations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthAllocationsApi->list_bandwidth_allocations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]

### Return type

[**BandwidthAllocationsListResponse**](BandwidthAllocationsListResponse.md)

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

# **update_bandwidth_allocations**
> BandwidthAllocations update_bandwidth_allocations(bandwidth_allocations=bandwidth_allocations)

Update a bandwidth allocation

Update an existing bandwidth allocation. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.bandwidth_allocations import BandwidthAllocations
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.BandwidthAllocationsApi(api_client)
    bandwidth_allocations = scm_deployment_services.BandwidthAllocations() # BandwidthAllocations | OK (optional)

    try:
        # Update a bandwidth allocation
        api_response = api_instance.update_bandwidth_allocations(bandwidth_allocations=bandwidth_allocations)
        print("The response of BandwidthAllocationsApi->update_bandwidth_allocations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthAllocationsApi->update_bandwidth_allocations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bandwidth_allocations** | [**BandwidthAllocations**](BandwidthAllocations.md)| OK | [optional] 

### Return type

[**BandwidthAllocations**](BandwidthAllocations.md)

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

