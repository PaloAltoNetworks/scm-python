# AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sdwan_gateway** | **str** | Next hop gateway | [optional] 
**sdwan_interface_profile** | **str** | SD-WAN interface profile | [optional] 
**upstream_nat** | [**AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettingsUpstreamNat**](AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettingsUpstreamNat.md) |  | [optional] 

## Example

```python
from scm_network_services.models.auto_vpn_clusters_branches_inner_interfaces_inner_sdwan_link_settings import AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettings from a JSON string
auto_vpn_clusters_branches_inner_interfaces_inner_sdwan_link_settings_instance = AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettings.from_json(json)
# print the JSON string representation of the object
print(AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettings.to_json())

# convert the object into a dict
auto_vpn_clusters_branches_inner_interfaces_inner_sdwan_link_settings_dict = auto_vpn_clusters_branches_inner_interfaces_inner_sdwan_link_settings_instance.to_dict()
# create an instance of AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettings from a dict
auto_vpn_clusters_branches_inner_interfaces_inner_sdwan_link_settings_from_dict = AutoVpnClustersBranchesInnerInterfacesInnerSdwanLinkSettings.from_dict(auto_vpn_clusters_branches_inner_interfaces_inner_sdwan_link_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


