# BgpRedistributionProfilesIpv4Unicast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | [**BgpRedistributionProfilesIpv4UnicastConnected**](BgpRedistributionProfilesIpv4UnicastConnected.md) |  | [optional] 
**ospf** | [**BgpRedistributionProfilesIpv4UnicastOspf**](BgpRedistributionProfilesIpv4UnicastOspf.md) |  | [optional] 
**static** | [**BgpRedistributionProfilesIpv4UnicastStatic**](BgpRedistributionProfilesIpv4UnicastStatic.md) |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_redistribution_profiles_ipv4_unicast import BgpRedistributionProfilesIpv4Unicast

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRedistributionProfilesIpv4Unicast from a JSON string
bgp_redistribution_profiles_ipv4_unicast_instance = BgpRedistributionProfilesIpv4Unicast.from_json(json)
# print the JSON string representation of the object
print(BgpRedistributionProfilesIpv4Unicast.to_json())

# convert the object into a dict
bgp_redistribution_profiles_ipv4_unicast_dict = bgp_redistribution_profiles_ipv4_unicast_instance.to_dict()
# create an instance of BgpRedistributionProfilesIpv4Unicast from a dict
bgp_redistribution_profiles_ipv4_unicast_from_dict = BgpRedistributionProfilesIpv4Unicast.from_dict(bgp_redistribution_profiles_ipv4_unicast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


