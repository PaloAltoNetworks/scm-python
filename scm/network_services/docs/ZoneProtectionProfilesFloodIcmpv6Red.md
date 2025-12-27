# ZoneProtectionProfilesFloodIcmpv6Red


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_rate** | **int** | The number of ICMPv6 packets (not matching an existing session) that the zone receives per second before subsequent ICMPv6 packets are dropped. | 
**alarm_rate** | **int** | The number of ICMPv6 echo requests (pings not matching an existing session) that the zone receives per second that triggers an attack alarm. | 
**maximal_rate** | **int** | The maximum number of ICMPv6 packets (not matching an existing session) that the zone receives per second before packets exceeding the maximum are dropped. | 

## Example

```python
from scm_network_services.models.zone_protection_profiles_flood_icmpv6_red import ZoneProtectionProfilesFloodIcmpv6Red

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodIcmpv6Red from a JSON string
zone_protection_profiles_flood_icmpv6_red_instance = ZoneProtectionProfilesFloodIcmpv6Red.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodIcmpv6Red.to_json())

# convert the object into a dict
zone_protection_profiles_flood_icmpv6_red_dict = zone_protection_profiles_flood_icmpv6_red_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodIcmpv6Red from a dict
zone_protection_profiles_flood_icmpv6_red_from_dict = ZoneProtectionProfilesFloodIcmpv6Red.from_dict(zone_protection_profiles_flood_icmpv6_red_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


