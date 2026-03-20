# BgpRedistributionProfilesIpv4UnicastConnected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable connected route redistribution? | [optional] 
**metric** | **int** | Route metric | [optional] 
**route_map** | **str** | Route map | [optional] 

## Example

```python
from scm.network_services.models.bgp_redistribution_profiles_ipv4_unicast_connected import BgpRedistributionProfilesIpv4UnicastConnected

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRedistributionProfilesIpv4UnicastConnected from a JSON string
bgp_redistribution_profiles_ipv4_unicast_connected_instance = BgpRedistributionProfilesIpv4UnicastConnected.from_json(json)
# print the JSON string representation of the object
print(BgpRedistributionProfilesIpv4UnicastConnected.to_json())

# convert the object into a dict
bgp_redistribution_profiles_ipv4_unicast_connected_dict = bgp_redistribution_profiles_ipv4_unicast_connected_instance.to_dict()
# create an instance of BgpRedistributionProfilesIpv4UnicastConnected from a dict
bgp_redistribution_profiles_ipv4_unicast_connected_from_dict = BgpRedistributionProfilesIpv4UnicastConnected.from_dict(bgp_redistribution_profiles_ipv4_unicast_connected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


