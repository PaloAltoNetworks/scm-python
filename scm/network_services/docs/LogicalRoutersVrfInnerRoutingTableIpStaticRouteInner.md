# LogicalRoutersVrfInnerRoutingTableIpStaticRouteInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_dist** | **int** |  | [optional] 
**bfd** | [**LogicalRoutersVrfInnerBgpGlobalBfd**](LogicalRoutersVrfInnerBgpGlobalBfd.md) |  | [optional] 
**destination** | **str** |  | [optional] 
**interface** | **str** |  | [optional] 
**metric** | **int** |  | [optional] 
**name** | **str** |  | 
**nexthop** | [**LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerNexthop**](LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerNexthop.md) |  | [optional] 
**path_monitor** | [**LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor**](LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor.md) |  | [optional] 
**route_table** | [**LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerRouteTable**](LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerRouteTable.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_routing_table_ip_static_route_inner import LogicalRoutersVrfInnerRoutingTableIpStaticRouteInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRoutingTableIpStaticRouteInner from a JSON string
logical_routers_vrf_inner_routing_table_ip_static_route_inner_instance = LogicalRoutersVrfInnerRoutingTableIpStaticRouteInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRoutingTableIpStaticRouteInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_routing_table_ip_static_route_inner_dict = logical_routers_vrf_inner_routing_table_ip_static_route_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRoutingTableIpStaticRouteInner from a dict
logical_routers_vrf_inner_routing_table_ip_static_route_inner_from_dict = LogicalRoutersVrfInnerRoutingTableIpStaticRouteInner.from_dict(logical_routers_vrf_inner_routing_table_ip_static_route_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


