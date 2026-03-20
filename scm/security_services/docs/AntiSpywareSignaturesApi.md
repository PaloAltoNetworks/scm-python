# scm.security_services.AntiSpywareSignaturesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_anti_spyware_signatures**](AntiSpywareSignaturesApi.md#create_anti_spyware_signatures) | **POST** /anti-spyware-signatures | Create an anti-spyware signature
[**delete_anti_spyware_signatures_by_id**](AntiSpywareSignaturesApi.md#delete_anti_spyware_signatures_by_id) | **DELETE** /anti-spyware-signatures/{id} | Delete an anti-spyware signature
[**get_anti_spyware_signatures_by_id**](AntiSpywareSignaturesApi.md#get_anti_spyware_signatures_by_id) | **GET** /anti-spyware-signatures/{id} | Get an anti-spyware signature
[**list_anti_spyware_signatures**](AntiSpywareSignaturesApi.md#list_anti_spyware_signatures) | **GET** /anti-spyware-signatures | List anti-spyware signatures
[**update_anti_spyware_signatures_by_id**](AntiSpywareSignaturesApi.md#update_anti_spyware_signatures_by_id) | **PUT** /anti-spyware-signatures/{id} | Update an anti-spyware signature


# **create_anti_spyware_signatures**
> AntiSpywareSignatures create_anti_spyware_signatures(anti_spyware_signatures=anti_spyware_signatures)

Create an anti-spyware signature

Create a new anti-spyware signature. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.anti_spyware_signatures import AntiSpywareSignatures
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
    api_instance = scm.security_services.AntiSpywareSignaturesApi(api_client)
    anti_spyware_signatures = scm.security_services.AntiSpywareSignatures() # AntiSpywareSignatures | Created (optional)

    try:
        # Create an anti-spyware signature
        api_response = api_instance.create_anti_spyware_signatures(anti_spyware_signatures=anti_spyware_signatures)
        print("The response of AntiSpywareSignaturesApi->create_anti_spyware_signatures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntiSpywareSignaturesApi->create_anti_spyware_signatures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anti_spyware_signatures** | [**AntiSpywareSignatures**](AntiSpywareSignatures.md)| Created | [optional] 

### Return type

[**AntiSpywareSignatures**](AntiSpywareSignatures.md)

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

# **delete_anti_spyware_signatures_by_id**
> delete_anti_spyware_signatures_by_id(id)

Delete an anti-spyware signature

Delete an anti-spyware signature. 

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
    api_instance = scm.security_services.AntiSpywareSignaturesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an anti-spyware signature
        api_instance.delete_anti_spyware_signatures_by_id(id)
    except Exception as e:
        print("Exception when calling AntiSpywareSignaturesApi->delete_anti_spyware_signatures_by_id: %s\n" % e)
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

# **get_anti_spyware_signatures_by_id**
> AntiSpywareSignatures get_anti_spyware_signatures_by_id(id)

Get an anti-spyware signature

Get an existing anti-spyware signature. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.anti_spyware_signatures import AntiSpywareSignatures
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
    api_instance = scm.security_services.AntiSpywareSignaturesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an anti-spyware signature
        api_response = api_instance.get_anti_spyware_signatures_by_id(id)
        print("The response of AntiSpywareSignaturesApi->get_anti_spyware_signatures_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntiSpywareSignaturesApi->get_anti_spyware_signatures_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**AntiSpywareSignatures**](AntiSpywareSignatures.md)

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

# **list_anti_spyware_signatures**
> AntiSpywareSignaturesListResponse list_anti_spyware_signatures(folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List anti-spyware signatures

Retrieve a list of anti-spyware signatures. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.anti_spyware_signatures_list_response import AntiSpywareSignaturesListResponse
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
    api_instance = scm.security_services.AntiSpywareSignaturesApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List anti-spyware signatures
        api_response = api_instance.list_anti_spyware_signatures(folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of AntiSpywareSignaturesApi->list_anti_spyware_signatures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntiSpywareSignaturesApi->list_anti_spyware_signatures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]

### Return type

[**AntiSpywareSignaturesListResponse**](AntiSpywareSignaturesListResponse.md)

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

# **update_anti_spyware_signatures_by_id**
> AntiSpywareSignatures update_anti_spyware_signatures_by_id(id, anti_spyware_signatures=anti_spyware_signatures)

Update an anti-spyware signature

Update an existing anti-spyware signature. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.anti_spyware_signatures import AntiSpywareSignatures
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
    api_instance = scm.security_services.AntiSpywareSignaturesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    anti_spyware_signatures = scm.security_services.AntiSpywareSignatures() # AntiSpywareSignatures | OK (optional)

    try:
        # Update an anti-spyware signature
        api_response = api_instance.update_anti_spyware_signatures_by_id(id, anti_spyware_signatures=anti_spyware_signatures)
        print("The response of AntiSpywareSignaturesApi->update_anti_spyware_signatures_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntiSpywareSignaturesApi->update_anti_spyware_signatures_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **anti_spyware_signatures** | [**AntiSpywareSignatures**](AntiSpywareSignatures.md)| OK | [optional] 

### Return type

[**AntiSpywareSignatures**](AntiSpywareSignatures.md)

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

