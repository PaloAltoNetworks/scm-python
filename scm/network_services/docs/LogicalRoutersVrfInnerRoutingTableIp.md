# LogicalRoutersVrfInnerRoutingTableIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_route** | [**List[LogicalRoutersVrfInnerRoutingTableIpStaticRouteInner]**](LogicalRoutersVrfInnerRoutingTableIpStaticRouteInner.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_routing_table_ip import LogicalRoutersVrfInnerRoutingTableIp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRoutingTableIp from a JSON string
logical_routers_vrf_inner_routing_table_ip_instance = LogicalRoutersVrfInnerRoutingTableIp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRoutingTableIp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_routing_table_ip_dict = logical_routers_vrf_inner_routing_table_ip_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRoutingTableIp from a dict
logical_routers_vrf_inner_routing_table_ip_from_dict = LogicalRoutersVrfInnerRoutingTableIp.from_dict(logical_routers_vrf_inner_routing_table_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


