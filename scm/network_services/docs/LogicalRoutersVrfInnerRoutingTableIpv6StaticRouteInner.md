# LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_dist** | **int** |  | [optional] 
**bfd** | [**LogicalRoutersVrfInnerBgpGlobalBfd**](LogicalRoutersVrfInnerBgpGlobalBfd.md) |  | [optional] 
**destination** | **str** |  | [optional] 
**interface** | **str** |  | [optional] 
**metric** | **int** |  | [optional] 
**name** | **str** |  | 
**nexthop** | [**LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerNexthop**](LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerNexthop.md) |  | [optional] 
**option** | [**LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerOption**](LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInnerOption.md) |  | [optional] 
**path_monitor** | [**LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor**](LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor.md) |  | [optional] 
**route_table** | [**LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerRouteTable**](LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerRouteTable.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_routing_table_ipv6_static_route_inner import LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInner from a JSON string
logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_instance = LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_dict = logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInner from a dict
logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_from_dict = LogicalRoutersVrfInnerRoutingTableIpv6StaticRouteInner.from_dict(logical_routers_vrf_inner_routing_table_ipv6_static_route_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


