# LogicalRoutersVrfInnerVrAdminDists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ebgp** | **int** |  | [optional] 
**ibgp** | **int** |  | [optional] 
**ospf_ext** | **int** |  | [optional] 
**ospf_int** | **int** |  | [optional] 
**ospfv3_ext** | **int** |  | [optional] 
**ospfv3_int** | **int** |  | [optional] 
**rip** | **int** |  | [optional] 
**static** | **int** |  | [optional] 
**static_ipv6** | **int** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_vr_admin_dists import LogicalRoutersVrfInnerVrAdminDists

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerVrAdminDists from a JSON string
logical_routers_vrf_inner_vr_admin_dists_instance = LogicalRoutersVrfInnerVrAdminDists.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerVrAdminDists.to_json())

# convert the object into a dict
logical_routers_vrf_inner_vr_admin_dists_dict = logical_routers_vrf_inner_vr_admin_dists_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerVrAdminDists from a dict
logical_routers_vrf_inner_vr_admin_dists_from_dict = LogicalRoutersVrfInnerVrAdminDists.from_dict(logical_routers_vrf_inner_vr_admin_dists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


