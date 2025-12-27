# ZoneProtectionProfilesFloodUdp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable protection against UDP floods? | [optional] 
**red** | [**ZoneProtectionProfilesFloodUdpRed**](ZoneProtectionProfilesFloodUdpRed.md) |  | [optional] 

## Example

```python
from scm.network_services.models.zone_protection_profiles_flood_udp import ZoneProtectionProfilesFloodUdp

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodUdp from a JSON string
zone_protection_profiles_flood_udp_instance = ZoneProtectionProfilesFloodUdp.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodUdp.to_json())

# convert the object into a dict
zone_protection_profiles_flood_udp_dict = zone_protection_profiles_flood_udp_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodUdp from a dict
zone_protection_profiles_flood_udp_from_dict = ZoneProtectionProfilesFloodUdp.from_dict(zone_protection_profiles_flood_udp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


