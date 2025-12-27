# AutoVpnClustersGatewaysInnerInterfacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_ip** | **str** | DHCP IP | [optional] 
**name** | **str** | Ethernet interface | [optional] 
**sdwan_link_settings** | [**AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettings**](AutoVpnClustersGatewaysInnerInterfacesInnerSdwanLinkSettings.md) |  | [optional] 

## Example

```python
from scm.network_services.models.auto_vpn_clusters_gateways_inner_interfaces_inner import AutoVpnClustersGatewaysInnerInterfacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnClustersGatewaysInnerInterfacesInner from a JSON string
auto_vpn_clusters_gateways_inner_interfaces_inner_instance = AutoVpnClustersGatewaysInnerInterfacesInner.from_json(json)
# print the JSON string representation of the object
print(AutoVpnClustersGatewaysInnerInterfacesInner.to_json())

# convert the object into a dict
auto_vpn_clusters_gateways_inner_interfaces_inner_dict = auto_vpn_clusters_gateways_inner_interfaces_inner_instance.to_dict()
# create an instance of AutoVpnClustersGatewaysInnerInterfacesInner from a dict
auto_vpn_clusters_gateways_inner_interfaces_inner_from_dict = AutoVpnClustersGatewaysInnerInterfacesInner.from_dict(auto_vpn_clusters_gateways_inner_interfaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


