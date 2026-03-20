# LogicalRoutersVrfInnerMulticastIgmpDynamicInterfaceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_filter** | **str** |  | [optional] 
**max_groups** | **str** |  | [optional] 
**max_sources** | **str** |  | [optional] 
**name** | **str** |  | 
**query_profile** | **str** |  | [optional] 
**robustness** | **str** |  | [optional] 
**router_alert_policing** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_igmp_dynamic_interface_inner import LogicalRoutersVrfInnerMulticastIgmpDynamicInterfaceInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastIgmpDynamicInterfaceInner from a JSON string
logical_routers_vrf_inner_multicast_igmp_dynamic_interface_inner_instance = LogicalRoutersVrfInnerMulticastIgmpDynamicInterfaceInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastIgmpDynamicInterfaceInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_igmp_dynamic_interface_inner_dict = logical_routers_vrf_inner_multicast_igmp_dynamic_interface_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastIgmpDynamicInterfaceInner from a dict
logical_routers_vrf_inner_multicast_igmp_dynamic_interface_inner_from_dict = LogicalRoutersVrfInnerMulticastIgmpDynamicInterfaceInner.from_dict(logical_routers_vrf_inner_multicast_igmp_dynamic_interface_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


