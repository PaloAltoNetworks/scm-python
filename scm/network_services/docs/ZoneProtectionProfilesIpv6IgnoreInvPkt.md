# ZoneProtectionProfilesIpv6IgnoreInvPkt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_unreach** | **bool** | Require an explicit Security policy match for Destination Unreachable ICMPv6 messages, even when the message is associated with an existing session. | [optional] 
**param_problem** | **bool** | Require an explicit Security policy match for Parameter Problem ICMPv6 messages, even when the message is associated with an existing session. | [optional] 
**pkt_too_big** | **bool** | Require an explicit Security policy match for Packet Too Big ICMPv6 messages, even when the message is associated with an existing session. | [optional] 
**redirect** | **bool** | Require an explicit Security policy match for Redirect Message ICMPv6 messages, even when the message is associated with an existing session. | [optional] 
**time_exceeded** | **bool** | Require an explicit Security policy match for Time Exceeded ICMPv6 messages, even when the message is associated with an existing session. | [optional] 

## Example

```python
from scm_network_services.models.zone_protection_profiles_ipv6_ignore_inv_pkt import ZoneProtectionProfilesIpv6IgnoreInvPkt

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesIpv6IgnoreInvPkt from a JSON string
zone_protection_profiles_ipv6_ignore_inv_pkt_instance = ZoneProtectionProfilesIpv6IgnoreInvPkt.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesIpv6IgnoreInvPkt.to_json())

# convert the object into a dict
zone_protection_profiles_ipv6_ignore_inv_pkt_dict = zone_protection_profiles_ipv6_ignore_inv_pkt_instance.to_dict()
# create an instance of ZoneProtectionProfilesIpv6IgnoreInvPkt from a dict
zone_protection_profiles_ipv6_ignore_inv_pkt_from_dict = ZoneProtectionProfilesIpv6IgnoreInvPkt.from_dict(zone_protection_profiles_ipv6_ignore_inv_pkt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


