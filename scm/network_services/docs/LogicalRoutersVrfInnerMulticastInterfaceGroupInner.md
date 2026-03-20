# LogicalRoutersVrfInnerMulticastInterfaceGroupInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**group_permission** | [**LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermission**](LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermission.md) |  | [optional] 
**igmp** | [**LogicalRoutersVrfInnerMulticastInterfaceGroupInnerIgmp**](LogicalRoutersVrfInnerMulticastInterfaceGroupInnerIgmp.md) |  | [optional] 
**interface** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**pim** | [**LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPim**](LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPim.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_interface_group_inner import LogicalRoutersVrfInnerMulticastInterfaceGroupInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastInterfaceGroupInner from a JSON string
logical_routers_vrf_inner_multicast_interface_group_inner_instance = LogicalRoutersVrfInnerMulticastInterfaceGroupInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastInterfaceGroupInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_interface_group_inner_dict = logical_routers_vrf_inner_multicast_interface_group_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastInterfaceGroupInner from a dict
logical_routers_vrf_inner_multicast_interface_group_inner_from_dict = LogicalRoutersVrfInnerMulticastInterfaceGroupInner.from_dict(logical_routers_vrf_inner_multicast_interface_group_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


