# LogicalRoutersVrfInnerBgpAggregateRoutesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_set** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**enable** | **bool** |  | [optional] 
**name** | **str** |  | 
**same_med** | **bool** |  | [optional] 
**summary_only** | **bool** |  | [optional] 
**type** | [**LogicalRoutersVrfInnerBgpAggregateRoutesInnerType**](LogicalRoutersVrfInnerBgpAggregateRoutesInnerType.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_aggregate_routes_inner import LogicalRoutersVrfInnerBgpAggregateRoutesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpAggregateRoutesInner from a JSON string
logical_routers_vrf_inner_bgp_aggregate_routes_inner_instance = LogicalRoutersVrfInnerBgpAggregateRoutesInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpAggregateRoutesInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_aggregate_routes_inner_dict = logical_routers_vrf_inner_bgp_aggregate_routes_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpAggregateRoutesInner from a dict
logical_routers_vrf_inner_bgp_aggregate_routes_inner_from_dict = LogicalRoutersVrfInnerBgpAggregateRoutesInner.from_dict(logical_routers_vrf_inner_bgp_aggregate_routes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


