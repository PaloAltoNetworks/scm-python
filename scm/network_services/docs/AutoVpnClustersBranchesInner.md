# AutoVpnClustersBranchesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_redistribution_profile** | **str** | BGP redistribution profile | [optional] 
**interfaces** | [**List[AutoVpnClustersBranchesInnerInterfacesInner]**](AutoVpnClustersBranchesInnerInterfacesInner.md) | Interfaces | [optional] 
**logical_router** | **str** | Router | [optional] 
**name** | **str** | Branch firewall serial number | [optional] 
**private_interfaces** | [**List[AutoVpnClustersBranchesInnerPrivateInterfacesInner]**](AutoVpnClustersBranchesInnerPrivateInterfacesInner.md) | Private interfaces | [optional] 
**site** | **str** | Site name | [optional] 

## Example

```python
from scm_network_services.models.auto_vpn_clusters_branches_inner import AutoVpnClustersBranchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnClustersBranchesInner from a JSON string
auto_vpn_clusters_branches_inner_instance = AutoVpnClustersBranchesInner.from_json(json)
# print the JSON string representation of the object
print(AutoVpnClustersBranchesInner.to_json())

# convert the object into a dict
auto_vpn_clusters_branches_inner_dict = auto_vpn_clusters_branches_inner_instance.to_dict()
# create an instance of AutoVpnClustersBranchesInner from a dict
auto_vpn_clusters_branches_inner_from_dict = AutoVpnClustersBranchesInner.from_dict(auto_vpn_clusters_branches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


