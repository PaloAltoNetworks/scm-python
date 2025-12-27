# BgpRouteMapsRouteMapInnerSetMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Metric action | [optional] 
**value** | **int** | Metric value | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_maps_route_map_inner_set_metric import BgpRouteMapsRouteMapInnerSetMetric

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapsRouteMapInnerSetMetric from a JSON string
bgp_route_maps_route_map_inner_set_metric_instance = BgpRouteMapsRouteMapInnerSetMetric.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapsRouteMapInnerSetMetric.to_json())

# convert the object into a dict
bgp_route_maps_route_map_inner_set_metric_dict = bgp_route_maps_route_map_inner_set_metric_instance.to_dict()
# create an instance of BgpRouteMapsRouteMapInnerSetMetric from a dict
bgp_route_maps_route_map_inner_set_metric_from_dict = BgpRouteMapsRouteMapInnerSetMetric.from_dict(bgp_route_maps_route_map_inner_set_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


