# ZoneProtectionProfilesFloodIcmp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable protection against ICMP floods? | [optional] 
**red** | [**ZoneProtectionProfilesFloodIcmpRed**](ZoneProtectionProfilesFloodIcmpRed.md) |  | [optional] 

## Example

```python
from scm.network_services.models.zone_protection_profiles_flood_icmp import ZoneProtectionProfilesFloodIcmp

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodIcmp from a JSON string
zone_protection_profiles_flood_icmp_instance = ZoneProtectionProfilesFloodIcmp.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodIcmp.to_json())

# convert the object into a dict
zone_protection_profiles_flood_icmp_dict = zone_protection_profiles_flood_icmp_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodIcmp from a dict
zone_protection_profiles_flood_icmp_from_dict = ZoneProtectionProfilesFloodIcmp.from_dict(zone_protection_profiles_flood_icmp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


