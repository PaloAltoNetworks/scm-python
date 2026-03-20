# LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**failure_condition** | **str** |  | [optional] 
**hold_time** | **int** |  | [optional] 
**monitor_destinations** | [**List[LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitorMonitorDestinationsInner]**](LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitorMonitorDestinationsInner.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_routing_table_ip_static_route_inner_path_monitor import LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor from a JSON string
logical_routers_vrf_inner_routing_table_ip_static_route_inner_path_monitor_instance = LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor.to_json())

# convert the object into a dict
logical_routers_vrf_inner_routing_table_ip_static_route_inner_path_monitor_dict = logical_routers_vrf_inner_routing_table_ip_static_route_inner_path_monitor_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor from a dict
logical_routers_vrf_inner_routing_table_ip_static_route_inner_path_monitor_from_dict = LogicalRoutersVrfInnerRoutingTableIpStaticRouteInnerPathMonitor.from_dict(logical_routers_vrf_inner_routing_table_ip_static_route_inner_path_monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


