# LogicalRoutersVrfInnerMulticastIgmp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic** | [**LogicalRoutersVrfInnerMulticastIgmpDynamic**](LogicalRoutersVrfInnerMulticastIgmpDynamic.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**static** | [**List[LogicalRoutersVrfInnerMulticastIgmpStaticInner]**](LogicalRoutersVrfInnerMulticastIgmpStaticInner.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_igmp import LogicalRoutersVrfInnerMulticastIgmp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastIgmp from a JSON string
logical_routers_vrf_inner_multicast_igmp_instance = LogicalRoutersVrfInnerMulticastIgmp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastIgmp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_igmp_dict = logical_routers_vrf_inner_multicast_igmp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastIgmp from a dict
logical_routers_vrf_inner_multicast_igmp_from_dict = LogicalRoutersVrfInnerMulticastIgmp.from_dict(logical_routers_vrf_inner_multicast_igmp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


