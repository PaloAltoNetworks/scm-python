# Zones


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**device_acl** | [**ZonesDeviceAcl**](ZonesDeviceAcl.md) |  | [optional] 
**dos_log_setting** | **str** |  | [optional] 
**dos_profile** | **str** |  | [optional] 
**enable_device_identification** | **bool** |  | [optional] 
**enable_user_identification** | **bool** |  | [optional] 
**folder** | **str** |  | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Alphanumeric string begin with letter: [0-9a-zA-Z._-] | 
**network** | [**ZonesNetwork**](ZonesNetwork.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**user_acl** | [**ZonesDeviceAcl**](ZonesDeviceAcl.md) |  | [optional] 

## Example

```python
from scm.network_services.models.zones import Zones

# TODO update the JSON string below
json = "{}"
# create an instance of Zones from a JSON string
zones_instance = Zones.from_json(json)
# print the JSON string representation of the object
print(Zones.to_json())

# convert the object into a dict
zones_dict = zones_instance.to_dict()
# create an instance of Zones from a dict
zones_from_dict = Zones.from_dict(zones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


