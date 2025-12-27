# HttpServerProfilesServerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | HTTP server address | [optional] 
**certificate_profile** | **str** | HTTP server certificate profile | [optional] [default to 'None']
**http_method** | **str** | HTTP operation to perform | [optional] 
**name** | **str** | HTTP server name | [optional] 
**port** | **int** | HTTP server port | [optional] 
**protocol** | **str** | HTTP server protocol | [optional] 
**tls_version** | **str** | HTTP server TLS version | [optional] 

## Example

```python
from scm_objects.models.http_server_profiles_server_inner import HttpServerProfilesServerInner

# TODO update the JSON string below
json = "{}"
# create an instance of HttpServerProfilesServerInner from a JSON string
http_server_profiles_server_inner_instance = HttpServerProfilesServerInner.from_json(json)
# print the JSON string representation of the object
print(HttpServerProfilesServerInner.to_json())

# convert the object into a dict
http_server_profiles_server_inner_dict = http_server_profiles_server_inner_instance.to_dict()
# create an instance of HttpServerProfilesServerInner from a dict
http_server_profiles_server_inner_from_dict = HttpServerProfilesServerInner.from_dict(http_server_profiles_server_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


