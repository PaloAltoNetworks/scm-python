# LogicalRoutersVrfInnerAdminDists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_external** | **int** |  | [optional] 
**bgp_internal** | **int** |  | [optional] 
**bgp_local** | **int** |  | [optional] 
**ospf_ext** | **int** |  | [optional] 
**ospf_inter** | **int** |  | [optional] 
**ospf_intra** | **int** |  | [optional] 
**ospfv3_ext** | **int** |  | [optional] 
**ospfv3_inter** | **int** |  | [optional] 
**ospfv3_intra** | **int** |  | [optional] 
**rip** | **int** |  | [optional] 
**static** | **int** |  | [optional] 
**static_ipv6** | **int** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_admin_dists import LogicalRoutersVrfInnerAdminDists

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerAdminDists from a JSON string
logical_routers_vrf_inner_admin_dists_instance = LogicalRoutersVrfInnerAdminDists.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerAdminDists.to_json())

# convert the object into a dict
logical_routers_vrf_inner_admin_dists_dict = logical_routers_vrf_inner_admin_dists_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerAdminDists from a dict
logical_routers_vrf_inner_admin_dists_from_dict = LogicalRoutersVrfInnerAdminDists.from_dict(logical_routers_vrf_inner_admin_dists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


