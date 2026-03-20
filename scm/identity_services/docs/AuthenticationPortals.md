# AuthenticationPortals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_profile** | **str** | The authentication profile | [optional] 
**certificate_profile** | **str** | The certificate profile | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**gp_udp_port** | **int** | The UDP port for inbound authentication prompts | [optional] 
**id** | **str** | The UUID of the authentication portal | [optional] [readonly] 
**idle_timer** | **int** | The idle timeout value (minutes) | [optional] 
**redirect_host** | **str** | The authentication portal IP address or hostname | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**timer** | **int** |  | [optional] 
**tls_service_profile** | **str** | The SSL/TLS service profile | [optional] 

## Example

```python
from scm.identity_services.models.authentication_portals import AuthenticationPortals

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationPortals from a JSON string
authentication_portals_instance = AuthenticationPortals.from_json(json)
# print the JSON string representation of the object
print(AuthenticationPortals.to_json())

# convert the object into a dict
authentication_portals_dict = authentication_portals_instance.to_dict()
# create an instance of AuthenticationPortals from a dict
authentication_portals_from_dict = AuthenticationPortals.from_dict(authentication_portals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


