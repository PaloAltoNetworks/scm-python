# LogicalRoutersVrfInnerMulticastStaticRouteInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** |  | [optional] 
**interface** | **str** |  | [optional] 
**name** | **str** |  | 
**nexthop** | [**LogicalRoutersVrfInnerMulticastStaticRouteInnerNexthop**](LogicalRoutersVrfInnerMulticastStaticRouteInnerNexthop.md) |  | [optional] 
**preference** | **int** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_static_route_inner import LogicalRoutersVrfInnerMulticastStaticRouteInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastStaticRouteInner from a JSON string
logical_routers_vrf_inner_multicast_static_route_inner_instance = LogicalRoutersVrfInnerMulticastStaticRouteInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastStaticRouteInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_static_route_inner_dict = logical_routers_vrf_inner_multicast_static_route_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastStaticRouteInner from a dict
logical_routers_vrf_inner_multicast_static_route_inner_from_dict = LogicalRoutersVrfInnerMulticastStaticRouteInner.from_dict(logical_routers_vrf_inner_multicast_static_route_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


