# ZoneProtectionProfilesScanInnerAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **object** |  | [optional] 
**allow** | **object** |  | [optional] 
**block** | **object** |  | [optional] 
**block_ip** | [**ZoneProtectionProfilesScanInnerActionBlockIp**](ZoneProtectionProfilesScanInnerActionBlockIp.md) |  | [optional] 

## Example

```python
from scm.network_services.models.zone_protection_profiles_scan_inner_action import ZoneProtectionProfilesScanInnerAction

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesScanInnerAction from a JSON string
zone_protection_profiles_scan_inner_action_instance = ZoneProtectionProfilesScanInnerAction.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesScanInnerAction.to_json())

# convert the object into a dict
zone_protection_profiles_scan_inner_action_dict = zone_protection_profiles_scan_inner_action_instance.to_dict()
# create an instance of ZoneProtectionProfilesScanInnerAction from a dict
zone_protection_profiles_scan_inner_action_from_dict = ZoneProtectionProfilesScanInnerAction.from_dict(zone_protection_profiles_scan_inner_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


