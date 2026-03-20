# ZoneProtectionProfilesFlood


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icmp** | [**ZoneProtectionProfilesFloodIcmp**](ZoneProtectionProfilesFloodIcmp.md) |  | [optional] 
**icmpv6** | [**ZoneProtectionProfilesFloodIcmpv6**](ZoneProtectionProfilesFloodIcmpv6.md) |  | [optional] 
**other_ip** | [**ZoneProtectionProfilesFloodOtherIp**](ZoneProtectionProfilesFloodOtherIp.md) |  | [optional] 
**sctp_init** | [**ZoneProtectionProfilesFloodSctpInit**](ZoneProtectionProfilesFloodSctpInit.md) |  | [optional] 
**tcp_syn** | [**ZoneProtectionProfilesFloodTcpSyn**](ZoneProtectionProfilesFloodTcpSyn.md) |  | [optional] 
**udp** | [**ZoneProtectionProfilesFloodUdp**](ZoneProtectionProfilesFloodUdp.md) |  | [optional] 

## Example

```python
from scm.network_services.models.zone_protection_profiles_flood import ZoneProtectionProfilesFlood

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFlood from a JSON string
zone_protection_profiles_flood_instance = ZoneProtectionProfilesFlood.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFlood.to_json())

# convert the object into a dict
zone_protection_profiles_flood_dict = zone_protection_profiles_flood_instance.to_dict()
# create an instance of ZoneProtectionProfilesFlood from a dict
zone_protection_profiles_flood_from_dict = ZoneProtectionProfilesFlood.from_dict(zone_protection_profiles_flood_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


