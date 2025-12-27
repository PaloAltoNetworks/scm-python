# LogicalRoutersVrfInnerMulticastIgmpStaticInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_address** | **str** |  | [optional] 
**interface** | **str** |  | [optional] 
**name** | **str** |  | 
**source_address** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_multicast_igmp_static_inner import LogicalRoutersVrfInnerMulticastIgmpStaticInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastIgmpStaticInner from a JSON string
logical_routers_vrf_inner_multicast_igmp_static_inner_instance = LogicalRoutersVrfInnerMulticastIgmpStaticInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastIgmpStaticInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_igmp_static_inner_dict = logical_routers_vrf_inner_multicast_igmp_static_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastIgmpStaticInner from a dict
logical_routers_vrf_inner_multicast_igmp_static_inner_from_dict = LogicalRoutersVrfInnerMulticastIgmpStaticInner.from_dict(logical_routers_vrf_inner_multicast_igmp_static_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


