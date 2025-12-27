# AutoVpnClustersBranchesInnerInterfacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_ip** | **str** | DHCP IP | [optional] 
**name** | **str** | Ethernet interface | [optional] 
**sdwan_link_settings** | [**AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettings**](AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettings.md) |  | [optional] 

## Example

```python
from scm_network_services.models.auto_vpn_clusters_branches_inner_interfaces_inner import AutoVpnClustersBranchesInnerInterfacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnClustersBranchesInnerInterfacesInner from a JSON string
auto_vpn_clusters_branches_inner_interfaces_inner_instance = AutoVpnClustersBranchesInnerInterfacesInner.from_json(json)
# print the JSON string representation of the object
print(AutoVpnClustersBranchesInnerInterfacesInner.to_json())

# convert the object into a dict
auto_vpn_clusters_branches_inner_interfaces_inner_dict = auto_vpn_clusters_branches_inner_interfaces_inner_instance.to_dict()
# create an instance of AutoVpnClustersBranchesInnerInterfacesInner from a dict
auto_vpn_clusters_branches_inner_interfaces_inner_from_dict = AutoVpnClustersBranchesInnerInterfacesInner.from_dict(auto_vpn_clusters_branches_inner_interfaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


