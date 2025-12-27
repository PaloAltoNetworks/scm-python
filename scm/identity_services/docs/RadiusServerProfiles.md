# RadiusServerProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the RADIUS server profile | [optional] [readonly] 
**name** | **str** | The name of the RADIUS server profile | 
**protocol** | [**RadiusServerProfilesProtocol**](RadiusServerProfilesProtocol.md) |  | 
**retries** | **int** | The number of RADIUS server retries | [optional] 
**server** | [**List[RadiusServerProfilesServerInner]**](RadiusServerProfilesServerInner.md) |  | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**timeout** | **int** | The RADIUS server authentication timeout (seconds) | [optional] 

## Example

```python
from scm_identity_services.models.radius_server_profiles import RadiusServerProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusServerProfiles from a JSON string
radius_server_profiles_instance = RadiusServerProfiles.from_json(json)
# print the JSON string representation of the object
print(RadiusServerProfiles.to_json())

# convert the object into a dict
radius_server_profiles_dict = radius_server_profiles_instance.to_dict()
# create an instance of RadiusServerProfiles from a dict
radius_server_profiles_from_dict = RadiusServerProfiles.from_dict(radius_server_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


