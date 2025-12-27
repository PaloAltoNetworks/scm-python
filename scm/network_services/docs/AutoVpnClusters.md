# AutoVpnClusters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branches** | [**List[AutoVpnClustersBranchesInner]**](AutoVpnClustersBranchesInner.md) | Branches | [optional] 
**enable_mesh_between_hubs** | **bool** | Enable mesh between hubs? | [optional] 
**enable_mesh_interconnect** | **bool** | Enable mesh interconnect? | [optional] 
**enable_sdwan** | **bool** | Enable SD-WAN? | [optional] 
**gateways** | [**List[AutoVpnClustersGatewaysInner]**](AutoVpnClustersGatewaysInner.md) | Hubs | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | VPN cluster name | [optional] 
**type** | **str** | VPN cluster type | [optional] [default to 'hub-spoke']

## Example

```python
from scm_network_services.models.auto_vpn_clusters import AutoVpnClusters

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnClusters from a JSON string
auto_vpn_clusters_instance = AutoVpnClusters.from_json(json)
# print the JSON string representation of the object
print(AutoVpnClusters.to_json())

# convert the object into a dict
auto_vpn_clusters_dict = auto_vpn_clusters_instance.to_dict()
# create an instance of AutoVpnClusters from a dict
auto_vpn_clusters_from_dict = AutoVpnClusters.from_dict(auto_vpn_clusters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


