# BgpAddressFamilyProfilesIpv4

IPv4 Address Family

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multicast** | [**BgpAddressFamily**](BgpAddressFamily.md) |  | [optional] 
**unicast** | [**BgpAddressFamily**](BgpAddressFamily.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_address_family_profiles_ipv4 import BgpAddressFamilyProfilesIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAddressFamilyProfilesIpv4 from a JSON string
bgp_address_family_profiles_ipv4_instance = BgpAddressFamilyProfilesIpv4.from_json(json)
# print the JSON string representation of the object
print(BgpAddressFamilyProfilesIpv4.to_json())

# convert the object into a dict
bgp_address_family_profiles_ipv4_dict = bgp_address_family_profiles_ipv4_instance.to_dict()
# create an instance of BgpAddressFamilyProfilesIpv4 from a dict
bgp_address_family_profiles_ipv4_from_dict = BgpAddressFamilyProfilesIpv4.from_dict(bgp_address_family_profiles_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


