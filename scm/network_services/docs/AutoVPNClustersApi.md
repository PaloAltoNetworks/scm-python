# scm.network_services.AutoVPNClustersApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_vpn_clusters**](AutoVPNClustersApi.md#create_auto_vpn_clusters) | **POST** /auto-vpn-clusters | Create an Auto VPN cluster
[**delete_auto_vpn_clusters_by_id**](AutoVPNClustersApi.md#delete_auto_vpn_clusters_by_id) | **DELETE** /auto-vpn-clusters/{id} | Delete an Auto VPN cluster
[**get_auto_vpn_clusters_by_id**](AutoVPNClustersApi.md#get_auto_vpn_clusters_by_id) | **GET** /auto-vpn-clusters/{id} | Get an Auto VPN cluster
[**list_auto_vpn_clusters**](AutoVPNClustersApi.md#list_auto_vpn_clusters) | **GET** /auto-vpn-clusters | List Auto VPN clusters
[**update_auto_vpn_clusters_by_id**](AutoVPNClustersApi.md#update_auto_vpn_clusters_by_id) | **PUT** /auto-vpn-clusters/{id} | Update an Auto VPN cluster


# **create_auto_vpn_clusters**
> AutoVpnClusters create_auto_vpn_clusters(auto_vpn_clusters=auto_vpn_clusters)

Create an Auto VPN cluster

Create a new Auto VPN cluster. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.auto_vpn_clusters import AutoVpnClusters
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
    api_instance = scm.network_services.AutoVPNClustersApi(api_client)
    auto_vpn_clusters = scm.network_services.AutoVpnClusters() # AutoVpnClusters | Created (optional)

    try:
        # Create an Auto VPN cluster
        api_response = api_instance.create_auto_vpn_clusters(auto_vpn_clusters=auto_vpn_clusters)
        print("The response of AutoVPNClustersApi->create_auto_vpn_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoVPNClustersApi->create_auto_vpn_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_vpn_clusters** | [**AutoVpnClusters**](AutoVpnClusters.md)| Created | [optional] 

### Return type

[**AutoVpnClusters**](AutoVpnClusters.md)

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

# **delete_auto_vpn_clusters_by_id**
> delete_auto_vpn_clusters_by_id(id)

Delete an Auto VPN cluster

Delete an Auto VPN cluster. 

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
    api_instance = scm.network_services.AutoVPNClustersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an Auto VPN cluster
        api_instance.delete_auto_vpn_clusters_by_id(id)
    except Exception as e:
        print("Exception when calling AutoVPNClustersApi->delete_auto_vpn_clusters_by_id: %s\n" % e)
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

# **get_auto_vpn_clusters_by_id**
> AutoVpnClusters get_auto_vpn_clusters_by_id(id)

Get an Auto VPN cluster

Get an existing Auto VPN clusters. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.auto_vpn_clusters import AutoVpnClusters
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
    api_instance = scm.network_services.AutoVPNClustersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an Auto VPN cluster
        api_response = api_instance.get_auto_vpn_clusters_by_id(id)
        print("The response of AutoVPNClustersApi->get_auto_vpn_clusters_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoVPNClustersApi->get_auto_vpn_clusters_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**AutoVpnClusters**](AutoVpnClusters.md)

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

# **list_auto_vpn_clusters**
> AutoVPNClustersListResponse list_auto_vpn_clusters(limit=limit, offset=offset, name=name)

List Auto VPN clusters

Retrieve a list of Auto VPN clusters. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.auto_vpn_clusters_list_response import AutoVPNClustersListResponse
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
    api_instance = scm.network_services.AutoVPNClustersApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)

    try:
        # List Auto VPN clusters
        api_response = api_instance.list_auto_vpn_clusters(limit=limit, offset=offset, name=name)
        print("The response of AutoVPNClustersApi->list_auto_vpn_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoVPNClustersApi->list_auto_vpn_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 

### Return type

[**AutoVPNClustersListResponse**](AutoVPNClustersListResponse.md)

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

# **update_auto_vpn_clusters_by_id**
> AutoVpnClusters update_auto_vpn_clusters_by_id(id, auto_vpn_clusters=auto_vpn_clusters)

Update an Auto VPN cluster

Update an existing Auto VPN cluster. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.auto_vpn_clusters import AutoVpnClusters
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
    api_instance = scm.network_services.AutoVPNClustersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    auto_vpn_clusters = scm.network_services.AutoVpnClusters() # AutoVpnClusters | OK (optional)

    try:
        # Update an Auto VPN cluster
        api_response = api_instance.update_auto_vpn_clusters_by_id(id, auto_vpn_clusters=auto_vpn_clusters)
        print("The response of AutoVPNClustersApi->update_auto_vpn_clusters_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoVPNClustersApi->update_auto_vpn_clusters_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **auto_vpn_clusters** | [**AutoVpnClusters**](AutoVpnClusters.md)| OK | [optional] 

### Return type

[**AutoVpnClusters**](AutoVpnClusters.md)

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

