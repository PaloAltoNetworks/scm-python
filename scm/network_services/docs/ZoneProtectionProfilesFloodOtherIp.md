# ZoneProtectionProfilesFloodOtherIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable protection against other IP (non-TCP, non-ICMP, non-ICMPv6, non-SCTP, and non-UDP) floods? | [optional] 
**red** | [**ZoneProtectionProfilesFloodOtherIpRed**](ZoneProtectionProfilesFloodOtherIpRed.md) |  | [optional] 

## Example

```python
from scm.network_services.models.zone_protection_profiles_flood_other_ip import ZoneProtectionProfilesFloodOtherIp

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodOtherIp from a JSON string
zone_protection_profiles_flood_other_ip_instance = ZoneProtectionProfilesFloodOtherIp.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodOtherIp.to_json())

# convert the object into a dict
zone_protection_profiles_flood_other_ip_dict = zone_protection_profiles_flood_other_ip_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodOtherIp from a dict
zone_protection_profiles_flood_other_ip_from_dict = ZoneProtectionProfilesFloodOtherIp.from_dict(zone_protection_profiles_flood_other_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


