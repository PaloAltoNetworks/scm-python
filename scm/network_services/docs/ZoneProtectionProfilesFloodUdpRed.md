# ZoneProtectionProfilesFloodUdpRed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_rate** | **int** | The number of UDP packets (not matching an existing session) that the zone receives per second that triggers random dropping of UDP packets. | 
**alarm_rate** | **int** | The number of UDP packets (not matching an existing session) that the zone receives per second that triggers an attack alarm. | 
**maximal_rate** | **int** | The maximum number of UDP packets (not matching an existing session) the zone receives per second before packets exceeding the maximum are dropped. | 

## Example

```python
from scm_network_services.models.zone_protection_profiles_flood_udp_red import ZoneProtectionProfilesFloodUdpRed

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodUdpRed from a JSON string
zone_protection_profiles_flood_udp_red_instance = ZoneProtectionProfilesFloodUdpRed.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodUdpRed.to_json())

# convert the object into a dict
zone_protection_profiles_flood_udp_red_dict = zone_protection_profiles_flood_udp_red_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodUdpRed from a dict
zone_protection_profiles_flood_udp_red_from_dict = ZoneProtectionProfilesFloodUdpRed.from_dict(zone_protection_profiles_flood_udp_red_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


