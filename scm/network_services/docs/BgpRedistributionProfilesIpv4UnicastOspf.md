# BgpRedistributionProfilesIpv4UnicastOspf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable OSPF route redistribution? | [optional] 
**metric** | **int** | Route metric | [optional] 
**route_map** | **str** | Route map | [optional] 

## Example

```python
from scm.network_services.models.bgp_redistribution_profiles_ipv4_unicast_ospf import BgpRedistributionProfilesIpv4UnicastOspf

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRedistributionProfilesIpv4UnicastOspf from a JSON string
bgp_redistribution_profiles_ipv4_unicast_ospf_instance = BgpRedistributionProfilesIpv4UnicastOspf.from_json(json)
# print the JSON string representation of the object
print(BgpRedistributionProfilesIpv4UnicastOspf.to_json())

# convert the object into a dict
bgp_redistribution_profiles_ipv4_unicast_ospf_dict = bgp_redistribution_profiles_ipv4_unicast_ospf_instance.to_dict()
# create an instance of BgpRedistributionProfilesIpv4UnicastOspf from a dict
bgp_redistribution_profiles_ipv4_unicast_ospf_from_dict = BgpRedistributionProfilesIpv4UnicastOspf.from_dict(bgp_redistribution_profiles_ipv4_unicast_ospf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


