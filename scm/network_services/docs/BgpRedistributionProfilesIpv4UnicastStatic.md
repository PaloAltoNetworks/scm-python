# BgpRedistributionProfilesIpv4UnicastStatic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable static route redistribution? | [optional] 
**metric** | **int** | Route metric | [optional] 
**route_map** | **str** | Route map | [optional] 

## Example

```python
from scm.network_services.models.bgp_redistribution_profiles_ipv4_unicast_static import BgpRedistributionProfilesIpv4UnicastStatic

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRedistributionProfilesIpv4UnicastStatic from a JSON string
bgp_redistribution_profiles_ipv4_unicast_static_instance = BgpRedistributionProfilesIpv4UnicastStatic.from_json(json)
# print the JSON string representation of the object
print(BgpRedistributionProfilesIpv4UnicastStatic.to_json())

# convert the object into a dict
bgp_redistribution_profiles_ipv4_unicast_static_dict = bgp_redistribution_profiles_ipv4_unicast_static_instance.to_dict()
# create an instance of BgpRedistributionProfilesIpv4UnicastStatic from a dict
bgp_redistribution_profiles_ipv4_unicast_static_from_dict = BgpRedistributionProfilesIpv4UnicastStatic.from_dict(bgp_redistribution_profiles_ipv4_unicast_static_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


