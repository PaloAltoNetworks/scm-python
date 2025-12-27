# scm_deployment_services.SitesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sites**](SitesApi.md#create_sites) | **POST** /sites | Create a site
[**delete_sites_by_id**](SitesApi.md#delete_sites_by_id) | **DELETE** /sites/{id} | Delete a site
[**get_sites_by_id**](SitesApi.md#get_sites_by_id) | **GET** /sites/{id} | Get a site
[**list_sites**](SitesApi.md#list_sites) | **GET** /sites | List sites
[**update_sites_by_id**](SitesApi.md#update_sites_by_id) | **PUT** /sites/{id} | Update a site


# **create_sites**
> Sites create_sites(sites=sites)

Create a site

Create a new sites.

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.sites import Sites
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
    api_instance = scm_deployment_services.SitesApi(api_client)
    sites = scm_deployment_services.Sites() # Sites | The site you want to create (optional)

    try:
        # Create a site
        api_response = api_instance.create_sites(sites=sites)
        print("The response of SitesApi->create_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->create_sites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sites** | [**Sites**](Sites.md)| The site you want to create | [optional] 

### Return type

[**Sites**](Sites.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sites_by_id**
> delete_sites_by_id(id)

Delete a site

Delete a site. 

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
    api_instance = scm_deployment_services.SitesApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Delete a site
        api_instance.delete_sites_by_id(id)
    except Exception as e:
        print("Exception when calling SitesApi->delete_sites_by_id: %s\n" % e)
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

# **get_sites_by_id**
> Sites get_sites_by_id(id)

Get a site

Get an existing site. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.sites import Sites
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
    api_instance = scm_deployment_services.SitesApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Get a site
        api_response = api_instance.get_sites_by_id(id)
        print("The response of SitesApi->get_sites_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->get_sites_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**Sites**](Sites.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a site&#39;s details by sdwan-site-id. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sites**
> SitesListResponse list_sites(folder, limit=limit, offset=offset, name=name)

List sites

Retrieve a list of sites.

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.sites_list_response import SitesListResponse
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
    api_instance = scm_deployment_services.SitesApi(api_client)
    folder = Remote Networks # str | The folder in which the resource is defined  (default to Remote Networks)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)

    try:
        # List sites
        api_response = api_instance.list_sites(folder, limit=limit, offset=offset, name=name)
        print("The response of SitesApi->list_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->list_sites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [default to Remote Networks]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 

### Return type

[**SitesListResponse**](SitesListResponse.md)

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

# **update_sites_by_id**
> Sites update_sites_by_id(id, sites=sites)

Update a site

Update an existing site. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.sites import Sites
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
    api_instance = scm_deployment_services.SitesApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource
    sites = scm_deployment_services.Sites() # Sites | The site you want to edit (optional)

    try:
        # Update a site
        api_response = api_instance.update_sites_by_id(id, sites=sites)
        print("The response of SitesApi->update_sites_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->update_sites_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **sites** | [**Sites**](Sites.md)| The site you want to edit | [optional] 

### Return type

[**Sites**](Sites.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

