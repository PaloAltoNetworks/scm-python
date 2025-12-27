# ZoneProtectionProfilesIpv6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anycast_source** | **bool** | Discard IPv6 packets that contain an anycast source address. | [optional] 
**filter_ext_hdr** | [**ZoneProtectionProfilesIpv6FilterExtHdr**](ZoneProtectionProfilesIpv6FilterExtHdr.md) |  | [optional] 
**icmpv6_too_big_small_mtu_discard** | **bool** | Discard IPv6 packets that contain a Packet Too Big ICMPv6 message when the maximum transmission unit (MTU) is less than 1,280 bytes. | [optional] 
**ignore_inv_pkt** | [**ZoneProtectionProfilesIpv6IgnoreInvPkt**](ZoneProtectionProfilesIpv6IgnoreInvPkt.md) |  | [optional] 
**ipv4_compatible_address** | **bool** | Discard IPv6 packets that are defined as an RFC 4291 IPv4-Compatible IPv6 address. | [optional] 
**needless_fragment_hdr** | **bool** | Discard IPv6 packets with the last fragment flag (M&#x3D;0) and offset of zero. | [optional] 
**options_invalid_ipv6_discard** | **bool** | Discard IPv6 packets that contain invalid IPv6 options in an extension header. | [optional] 
**reserved_field_set_discard** | **bool** | Discard IPv6 packets that have a header with a reserved field not set to zero. | [optional] 
**routing_header_0** | **bool** | Drop packets with type 0 routing header. | [optional] 
**routing_header_1** | **bool** | Drop packets with type 1 routing header. | [optional] 
**routing_header_253** | **bool** | Drop packets with type 253 routing header. | [optional] 
**routing_header_254** | **bool** | Drop packets with type 254 routing header. | [optional] 
**routing_header_255** | **bool** | Drop packets with type 255 routing header. | [optional] 
**routing_header_3** | **bool** | Drop packets with type 3 routing header. | [optional] 
**routing_header_4_252** | **bool** | Drop packets with type 4 to type 252 routing header. | [optional] 

## Example

```python
from scm.network_services.models.zone_protection_profiles_ipv6 import ZoneProtectionProfilesIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesIpv6 from a JSON string
zone_protection_profiles_ipv6_instance = ZoneProtectionProfilesIpv6.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesIpv6.to_json())

# convert the object into a dict
zone_protection_profiles_ipv6_dict = zone_protection_profiles_ipv6_instance.to_dict()
# create an instance of ZoneProtectionProfilesIpv6 from a dict
zone_protection_profiles_ipv6_from_dict = ZoneProtectionProfilesIpv6.from_dict(zone_protection_profiles_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


