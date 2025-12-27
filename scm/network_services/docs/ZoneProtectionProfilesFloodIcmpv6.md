# ZoneProtectionProfilesFloodIcmpv6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable protection against ICMPv6 floods? | [optional] 
**red** | [**ZoneProtectionProfilesFloodIcmpv6Red**](ZoneProtectionProfilesFloodIcmpv6Red.md) |  | [optional] 

## Example

```python
from scm_network_services.models.zone_protection_profiles_flood_icmpv6 import ZoneProtectionProfilesFloodIcmpv6

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodIcmpv6 from a JSON string
zone_protection_profiles_flood_icmpv6_instance = ZoneProtectionProfilesFloodIcmpv6.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodIcmpv6.to_json())

# convert the object into a dict
zone_protection_profiles_flood_icmpv6_dict = zone_protection_profiles_flood_icmpv6_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodIcmpv6 from a dict
zone_protection_profiles_flood_icmpv6_from_dict = ZoneProtectionProfilesFloodIcmpv6.from_dict(zone_protection_profiles_flood_icmpv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


