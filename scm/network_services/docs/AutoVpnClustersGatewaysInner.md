# AutoVpnClustersGatewaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_dia_vpn_failover** | **bool** | Allow DIA to VPN failover on branch device for the hub? | [optional] 
**bgp_redistribution_profile** | **str** | BGP redistribution file | [optional] 
**interfaces** | [**List[AutoVpnClustersGatewaysInnerInterfacesInner]**](AutoVpnClustersGatewaysInnerInterfacesInner.md) | Interfaces | [optional] 
**logical_router** | **str** | Router | [optional] 
**name** | **str** | Hub firewall serial number | [optional] 
**priority** | **str** | Priority | [optional] 
**private_interfaces** | [**List[AutoVpnClustersGatewaysInnerPrivateInterfacesInner]**](AutoVpnClustersGatewaysInnerPrivateInterfacesInner.md) | Private interfaces | [optional] 
**site** | **str** | Site name | [optional] 

## Example

```python
from scm.network_services.models.auto_vpn_clusters_gateways_inner import AutoVpnClustersGatewaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnClustersGatewaysInner from a JSON string
auto_vpn_clusters_gateways_inner_instance = AutoVpnClustersGatewaysInner.from_json(json)
# print the JSON string representation of the object
print(AutoVpnClustersGatewaysInner.to_json())

# convert the object into a dict
auto_vpn_clusters_gateways_inner_dict = auto_vpn_clusters_gateways_inner_instance.to_dict()
# create an instance of AutoVpnClustersGatewaysInner from a dict
auto_vpn_clusters_gateways_inner_from_dict = AutoVpnClustersGatewaysInner.from_dict(auto_vpn_clusters_gateways_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


