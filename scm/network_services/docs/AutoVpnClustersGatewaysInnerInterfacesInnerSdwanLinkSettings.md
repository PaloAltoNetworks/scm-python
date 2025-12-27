# AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sdwan_gateway** | **str** | Next hop gateway | [optional] 
**sdwan_interface_profile** | **str** | SD-WAN interface profile | [optional] 
**upstream_nat** | [**AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettingsUpstreamNat**](AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettingsUpstreamNat.md) |  | [optional] 

## Example

```python
from scm_network_services.models.auto_vpn_clusters_gateways_inner_interfaces_inner_sdwan_link_settings import AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettings from a JSON string
auto_vpn_clusters_gateways_inner_interfaces_inner_sdwan_link_settings_instance = AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettings.from_json(json)
# print the JSON string representation of the object
print(AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettings.to_json())

# convert the object into a dict
auto_vpn_clusters_gateways_inner_interfaces_inner_sdwan_link_settings_dict = auto_vpn_clusters_gateways_inner_interfaces_inner_sdwan_link_settings_instance.to_dict()
# create an instance of AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettings from a dict
auto_vpn_clusters_gateways_inner_interfaces_inner_sdwan_link_settings_from_dict = AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettings.from_dict(auto_vpn_clusters_gateways_inner_interfaces_inner_sdwan_link_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


