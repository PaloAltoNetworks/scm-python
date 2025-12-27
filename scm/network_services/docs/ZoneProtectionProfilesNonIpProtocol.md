# ZoneProtectionProfilesNonIpProtocol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_type** | **str** | Specify the type of list you are creating for protocol protection: * Include List—Only the protocols on the list are allowed—in addition to IPv4 (0x0800), IPv6 (0x86DD), ARP (0x0806), and VLAN tagged frames (0x8100). All other protocols are implicitly denied (blocked). * Exclude List—Only the protocols on the list are denied; all other protocols are implicitly allowed. You cannot exclude IPv4 (0x0800), IPv6 (0x86DD), ARP (0x0806), or VLAN tagged frames (0x8100).  | [optional] 
**protocol** | [**List[ZoneProtectionProfilesNonIpProtocolProtocolInner]**](ZoneProtectionProfilesNonIpProtocolProtocolInner.md) |  | [optional] 

## Example

```python
from scm_network_services.models.zone_protection_profiles_non_ip_protocol import ZoneProtectionProfilesNonIpProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesNonIpProtocol from a JSON string
zone_protection_profiles_non_ip_protocol_instance = ZoneProtectionProfilesNonIpProtocol.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesNonIpProtocol.to_json())

# convert the object into a dict
zone_protection_profiles_non_ip_protocol_dict = zone_protection_profiles_non_ip_protocol_instance.to_dict()
# create an instance of ZoneProtectionProfilesNonIpProtocol from a dict
zone_protection_profiles_non_ip_protocol_from_dict = ZoneProtectionProfilesNonIpProtocol.from_dict(zone_protection_profiles_non_ip_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


