# ZoneProtectionProfilesIpv6FilterExtHdr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_option_hdr** | **bool** | Discard IPv6 packets that contain the Destination Options extension, which contains options intended only for the destination of the packet. | [optional] 
**hop_by_hop_hdr** | **bool** | Discard IPv6 packets that contain the Hop-by-Hop Options extension header. | [optional] 
**routing_hdr** | **bool** | Discard IPv6 packets that contain the Routing extension header, which directs packets to one or more intermediate nodes on its way to its destination. | [optional] 

## Example

```python
from scm_network_services.models.zone_protection_profiles_ipv6_filter_ext_hdr import ZoneProtectionProfilesIpv6FilterExtHdr

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesIpv6FilterExtHdr from a JSON string
zone_protection_profiles_ipv6_filter_ext_hdr_instance = ZoneProtectionProfilesIpv6FilterExtHdr.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesIpv6FilterExtHdr.to_json())

# convert the object into a dict
zone_protection_profiles_ipv6_filter_ext_hdr_dict = zone_protection_profiles_ipv6_filter_ext_hdr_instance.to_dict()
# create an instance of ZoneProtectionProfilesIpv6FilterExtHdr from a dict
zone_protection_profiles_ipv6_filter_ext_hdr_from_dict = ZoneProtectionProfilesIpv6FilterExtHdr.from_dict(zone_protection_profiles_ipv6_filter_ext_hdr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


