# RadiusServerProfilesServerInner

The RADIUS server configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | The IP address of the RADIUS server | [optional] 
**name** | **str** | The name of the RADIUS server | [optional] 
**port** | **int** | The RADIUS server port | [optional] 
**secret** | **str** | The RADIUS secret | [optional] 

## Example

```python
from scm_identity_services.models.radius_server_profiles_server_inner import RadiusServerProfilesServerInner

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusServerProfilesServerInner from a JSON string
radius_server_profiles_server_inner_instance = RadiusServerProfilesServerInner.from_json(json)
# print the JSON string representation of the object
print(RadiusServerProfilesServerInner.to_json())

# convert the object into a dict
radius_server_profiles_server_inner_dict = radius_server_profiles_server_inner_instance.to_dict()
# create an instance of RadiusServerProfilesServerInner from a dict
radius_server_profiles_server_inner_from_dict = RadiusServerProfilesServerInner.from_dict(radius_server_profiles_server_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


