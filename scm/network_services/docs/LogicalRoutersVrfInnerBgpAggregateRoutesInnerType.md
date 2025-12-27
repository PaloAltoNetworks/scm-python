# LogicalRoutersVrfInnerBgpAggregateRoutesInnerType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | [**LogicalRoutersVrfInnerBgpAggregateRoutesInnerTypeIpv4**](LogicalRoutersVrfInnerBgpAggregateRoutesInnerTypeIpv4.md) |  | [optional] 
**ipv6** | [**LogicalRoutersVrfInnerBgpAggregateRoutesInnerTypeIpv4**](LogicalRoutersVrfInnerBgpAggregateRoutesInnerTypeIpv4.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_aggregate_routes_inner_type import LogicalRoutersVrfInnerBgpAggregateRoutesInnerType

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpAggregateRoutesInnerType from a JSON string
logical_routers_vrf_inner_bgp_aggregate_routes_inner_type_instance = LogicalRoutersVrfInnerBgpAggregateRoutesInnerType.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpAggregateRoutesInnerType.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_aggregate_routes_inner_type_dict = logical_routers_vrf_inner_bgp_aggregate_routes_inner_type_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpAggregateRoutesInnerType from a dict
logical_routers_vrf_inner_bgp_aggregate_routes_inner_type_from_dict = LogicalRoutersVrfInnerBgpAggregateRoutesInnerType.from_dict(logical_routers_vrf_inner_bgp_aggregate_routes_inner_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


