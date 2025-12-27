# LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerNexthop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discard** | **object** |  | [optional] 
**fqdn** | **str** |  | [optional] 
**ipv6_address** | **str** |  | [optional] 
**next_lr** | **str** |  | [optional] 
**next_vr** | **str** |  | [optional] 
**receive** | **object** |  | [optional] 
**tunnel** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_nexthop import LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerNexthop

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerNexthop from a JSON string
logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_nexthop_instance = LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerNexthop.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerNexthop.to_json())

# convert the object into a dict
logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_nexthop_dict = logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_nexthop_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerNexthop from a dict
logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_nexthop_from_dict = LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerNexthop.from_dict(logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_nexthop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


