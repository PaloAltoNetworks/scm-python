# BgpRouteMapsRouteMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action | [optional] 
**description** | **str** | Description | [optional] 
**match** | [**BgpRouteMapsRouteMapInnerMatch**](BgpRouteMapsRouteMapInnerMatch.md) |  | [optional] 
**name** | **int** | Sequence number | [optional] 
**set** | [**BgpRouteMapsRouteMapInnerSet**](BgpRouteMapsRouteMapInnerSet.md) |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_maps_route_map_inner import BgpRouteMapsRouteMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapsRouteMapInner from a JSON string
bgp_route_maps_route_map_inner_instance = BgpRouteMapsRouteMapInner.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapsRouteMapInner.to_json())

# convert the object into a dict
bgp_route_maps_route_map_inner_dict = bgp_route_maps_route_map_inner_instance.to_dict()
# create an instance of BgpRouteMapsRouteMapInner from a dict
bgp_route_maps_route_map_inner_from_dict = BgpRouteMapsRouteMapInner.from_dict(bgp_route_maps_route_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


