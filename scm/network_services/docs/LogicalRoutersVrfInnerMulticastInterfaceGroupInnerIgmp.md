# LogicalRoutersVrfInnerMulticastInterfaceGroupInnerIgmp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**immediate_leave** | **bool** |  | [optional] 
**last_member_query_interval** | **int** |  | [optional] 
**max_groups** | **str** |  | [optional] 
**max_query_response_time** | **int** |  | [optional] 
**max_sources** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**query_interval** | **int** |  | [optional] 
**robustness** | **str** |  | [optional] 
**router_alert_policing** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_interface_group_inner_igmp import LogicalRoutersVrfInnerMulticastInterfaceGroupInnerIgmp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastInterfaceGroupInnerIgmp from a JSON string
logical_routers_vrf_inner_multicast_interface_group_inner_igmp_instance = LogicalRoutersVrfInnerMulticastInterfaceGroupInnerIgmp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastInterfaceGroupInnerIgmp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_interface_group_inner_igmp_dict = logical_routers_vrf_inner_multicast_interface_group_inner_igmp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastInterfaceGroupInnerIgmp from a dict
logical_routers_vrf_inner_multicast_interface_group_inner_igmp_from_dict = LogicalRoutersVrfInnerMulticastInterfaceGroupInnerIgmp.from_dict(logical_routers_vrf_inner_multicast_interface_group_inner_igmp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


