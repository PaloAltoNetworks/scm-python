# LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_neighbors** | [**List[LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPimAllowedNeighborsInner]**](LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPimAllowedNeighborsInner.md) |  | [optional] 
**assert_interval** | **int** |  | [optional] 
**bsr_border** | **bool** |  | [optional] 
**dr_priority** | **int** |  | [optional] 
**enable** | **bool** |  | [optional] 
**hello_interval** | **int** |  | [optional] 
**join_prune_interval** | **int** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_interface_group_inner_pim import LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPim

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPim from a JSON string
logical_routers_vrf_inner_multicast_interface_group_inner_pim_instance = LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPim.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPim.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_interface_group_inner_pim_dict = logical_routers_vrf_inner_multicast_interface_group_inner_pim_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPim from a dict
logical_routers_vrf_inner_multicast_interface_group_inner_pim_from_dict = LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPim.from_dict(logical_routers_vrf_inner_multicast_interface_group_inner_pim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


