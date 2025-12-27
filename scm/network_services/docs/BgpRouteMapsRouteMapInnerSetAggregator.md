# BgpRouteMapsRouteMapInnerSetAggregator

bgp-route-maps aggregator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_as** | **int** | Aggregator AS | [optional] 
**router_id** | **str** | Router ID | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_maps_route_map_inner_set_aggregator import BgpRouteMapsRouteMapInnerSetAggregator

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapsRouteMapInnerSetAggregator from a JSON string
bgp_route_maps_route_map_inner_set_aggregator_instance = BgpRouteMapsRouteMapInnerSetAggregator.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapsRouteMapInnerSetAggregator.to_json())

# convert the object into a dict
bgp_route_maps_route_map_inner_set_aggregator_dict = bgp_route_maps_route_map_inner_set_aggregator_instance.to_dict()
# create an instance of BgpRouteMapsRouteMapInnerSetAggregator from a dict
bgp_route_maps_route_map_inner_set_aggregator_from_dict = BgpRouteMapsRouteMapInnerSetAggregator.from_dict(bgp_route_maps_route_map_inner_set_aggregator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


