# ZoneProtectionProfilesFloodIcmpRed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_rate** | **int** | The number of ICMP packets (not matching an existing session) that the zone receives per second before subsequent ICMP packets are dropped. | 
**alarm_rate** | **int** | The number of ICMP echo requests (pings not matching an existing session) that the zone receives per second that triggers an attack alarm. | 
**maximal_rate** | **int** | The maximum number of ICMP packets (not matching an existing session) that the zone receives per second before packets exceeding the maximum are dropped. | 

## Example

```python
from scm_network_services.models.zone_protection_profiles_flood_icmp_red import ZoneProtectionProfilesFloodIcmpRed

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodIcmpRed from a JSON string
zone_protection_profiles_flood_icmp_red_instance = ZoneProtectionProfilesFloodIcmpRed.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodIcmpRed.to_json())

# convert the object into a dict
zone_protection_profiles_flood_icmp_red_dict = zone_protection_profiles_flood_icmp_red_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodIcmpRed from a dict
zone_protection_profiles_flood_icmp_red_from_dict = ZoneProtectionProfilesFloodIcmpRed.from_dict(zone_protection_profiles_flood_icmp_red_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


