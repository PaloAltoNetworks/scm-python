# ZoneProtectionProfilesFloodSctpInitRed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_rate** | **int** | The number of SCTP INIT packets (not matching an existing session) that the zone receives per second before subsequent SCTP INIT packets are dropped. | 
**alarm_rate** | **int** | The number of SCTP INIT packets (not matching an existing session) that the zone receives per second that triggers an attack alarm. | 
**maximal_rate** | **int** | The maximum number of SCTP INIT packets (not matching an existing session) that the zone receives per second before packets exceeding the maximum are dropped. | 

## Example

```python
from scm.network_services.models.zone_protection_profiles_flood_sctp_init_red import ZoneProtectionProfilesFloodSctpInitRed

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodSctpInitRed from a JSON string
zone_protection_profiles_flood_sctp_init_red_instance = ZoneProtectionProfilesFloodSctpInitRed.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodSctpInitRed.to_json())

# convert the object into a dict
zone_protection_profiles_flood_sctp_init_red_dict = zone_protection_profiles_flood_sctp_init_red_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodSctpInitRed from a dict
zone_protection_profiles_flood_sctp_init_red_from_dict = ZoneProtectionProfilesFloodSctpInitRed.from_dict(zone_protection_profiles_flood_sctp_init_red_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


