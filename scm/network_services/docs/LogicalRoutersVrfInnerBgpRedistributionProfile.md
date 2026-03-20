# LogicalRoutersVrfInnerBgpRedistributionProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | [**LogicalRoutersVrfInnerBgpRedistributionProfileIpv4**](LogicalRoutersVrfInnerBgpRedistributionProfileIpv4.md) |  | [optional] 
**ipv6** | [**LogicalRoutersVrfInnerBgpRedistributionProfileIpv4**](LogicalRoutersVrfInnerBgpRedistributionProfileIpv4.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_redistribution_profile import LogicalRoutersVrfInnerBgpRedistributionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpRedistributionProfile from a JSON string
logical_routers_vrf_inner_bgp_redistribution_profile_instance = LogicalRoutersVrfInnerBgpRedistributionProfile.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpRedistributionProfile.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_redistribution_profile_dict = logical_routers_vrf_inner_bgp_redistribution_profile_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpRedistributionProfile from a dict
logical_routers_vrf_inner_bgp_redistribution_profile_from_dict = LogicalRoutersVrfInnerBgpRedistributionProfile.from_dict(logical_routers_vrf_inner_bgp_redistribution_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


