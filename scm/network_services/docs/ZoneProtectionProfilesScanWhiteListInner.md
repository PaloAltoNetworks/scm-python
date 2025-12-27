# ZoneProtectionProfilesScanWhiteListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | **str** |  | [optional] 
**ipv6** | **str** |  | [optional] 
**name** | **str** | A descriptive name for the address to exclude. | 

## Example

```python
from scm.network_services.models.zone_protection_profiles_scan_white_list_inner import ZoneProtectionProfilesScanWhiteListInner

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesScanWhiteListInner from a JSON string
zone_protection_profiles_scan_white_list_inner_instance = ZoneProtectionProfilesScanWhiteListInner.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesScanWhiteListInner.to_json())

# convert the object into a dict
zone_protection_profiles_scan_white_list_inner_dict = zone_protection_profiles_scan_white_list_inner_instance.to_dict()
# create an instance of ZoneProtectionProfilesScanWhiteListInner from a dict
zone_protection_profiles_scan_white_list_inner_from_dict = ZoneProtectionProfilesScanWhiteListInner.from_dict(zone_protection_profiles_scan_white_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


