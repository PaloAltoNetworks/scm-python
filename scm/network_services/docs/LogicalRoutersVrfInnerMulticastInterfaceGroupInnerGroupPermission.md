# LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any_source_multicast** | [**List[LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermissionAnySourceMulticastInner]**](LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermissionAnySourceMulticastInner.md) |  | [optional] 
**source_specific_multicast** | [**List[LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermissionSourceSpecificMulticastInner]**](LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermissionSourceSpecificMulticastInner.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_multicast_interface_group_inner_group_permission import LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermission

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermission from a JSON string
logical_routers_vrf_inner_multicast_interface_group_inner_group_permission_instance = LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermission.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermission.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_interface_group_inner_group_permission_dict = logical_routers_vrf_inner_multicast_interface_group_inner_group_permission_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermission from a dict
logical_routers_vrf_inner_multicast_interface_group_inner_group_permission_from_dict = LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermission.from_dict(logical_routers_vrf_inner_multicast_interface_group_inner_group_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


