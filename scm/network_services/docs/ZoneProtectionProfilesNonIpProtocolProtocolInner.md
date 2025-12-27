# ZoneProtectionProfilesNonIpProtocolProtocolInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable the Ethertype code on the list. | [optional] 
**ether_type** | **str** | Enter an Ethertype code (protocol) preceded by 0x to indicate hexadecimal (range is 0x0000 to 0xFFFF). A list can have a maximum of 64 Ethertypes. Some sources of Ethertype codes are: * [IEEE hexadecimal Ethertype](https://www.iana.org/assignments/ieee-802-numbers/ieee-802-numbers.xhtml) * [standards.ieee.org/develop/regauth/ethertype/eth.txt](https://standards-oui.ieee.org/ethertype/eth.txt) * [www.cavebear.com/archive/cavebear/Ethernet/type.html](https://www.cavebear.com/archive/cavebear/Ethernet/type.html)  | 
**name** | **str** | Enter the protocol name that corresponds to the Ethertype code you are adding to the list. The firewall does not verify that the protocol name matches the Ethertype code but the Ethertype code does determine the protocol filter.  | 

## Example

```python
from scm_network_services.models.zone_protection_profiles_non_ip_protocol_protocol_inner import ZoneProtectionProfilesNonIpProtocolProtocolInner

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesNonIpProtocolProtocolInner from a JSON string
zone_protection_profiles_non_ip_protocol_protocol_inner_instance = ZoneProtectionProfilesNonIpProtocolProtocolInner.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesNonIpProtocolProtocolInner.to_json())

# convert the object into a dict
zone_protection_profiles_non_ip_protocol_protocol_inner_dict = zone_protection_profiles_non_ip_protocol_protocol_inner_instance.to_dict()
# create an instance of ZoneProtectionProfilesNonIpProtocolProtocolInner from a dict
zone_protection_profiles_non_ip_protocol_protocol_inner_from_dict = ZoneProtectionProfilesNonIpProtocolProtocolInner.from_dict(zone_protection_profiles_non_ip_protocol_protocol_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


