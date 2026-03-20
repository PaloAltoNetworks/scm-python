# LogicalRoutersVrfInnerMulticastPimInterfaceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**dr_priority** | **int** |  | [optional] 
**if_timer** | **str** |  | [optional] 
**name** | **str** |  | 
**neighbor_filter** | **str** |  | [optional] 
**send_bsm** | **bool** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_pim_interface_inner import LogicalRoutersVrfInnerMulticastPimInterfaceInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastPimInterfaceInner from a JSON string
logical_routers_vrf_inner_multicast_pim_interface_inner_instance = LogicalRoutersVrfInnerMulticastPimInterfaceInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastPimInterfaceInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_pim_interface_inner_dict = logical_routers_vrf_inner_multicast_pim_interface_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastPimInterfaceInner from a dict
logical_routers_vrf_inner_multicast_pim_interface_inner_from_dict = LogicalRoutersVrfInnerMulticastPimInterfaceInner.from_dict(logical_routers_vrf_inner_multicast_pim_interface_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


