# BgpRouteMapsRouteMapInnerSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregator** | [**BgpRouteMapsRouteMapInnerSetAggregator**](BgpRouteMapsRouteMapInnerSetAggregator.md) |  | [optional] 
**aspath_exclude** | **List[int]** |  | [optional] 
**aspath_prepend** | **List[int]** |  | [optional] 
**atomic_aggregate** | **bool** | Enable BGP atomic aggregate? | [optional] 
**ipv4** | [**BgpRouteMapsRouteMapInnerSetIpv4**](BgpRouteMapsRouteMapInnerSetIpv4.md) |  | [optional] 
**large_community** | **List[str]** |  | [optional] 
**local_preference** | **int** | Local preference | [optional] 
**metric** | [**BgpRouteMapsRouteMapInnerSetMetric**](BgpRouteMapsRouteMapInnerSetMetric.md) |  | [optional] 
**origin** | **str** | Origin | [optional] 
**originator_id** | **str** | Originator ID | [optional] 
**overwrite_large_community** | **bool** | Overwrite large community? | [optional] 
**overwrite_regular_community** | **bool** | Overwrite regular community? | [optional] 
**regular_community** | **List[str]** |  | [optional] 
**remove_large_community** | **str** | Remove large community name | [optional] 
**remove_regular_community** | **str** | Remove regular community name | [optional] 
**tag** | **int** | Tag | [optional] 
**weight** | **int** | Weight | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_maps_route_map_inner_set import BgpRouteMapsRouteMapInnerSet

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapsRouteMapInnerSet from a JSON string
bgp_route_maps_route_map_inner_set_instance = BgpRouteMapsRouteMapInnerSet.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapsRouteMapInnerSet.to_json())

# convert the object into a dict
bgp_route_maps_route_map_inner_set_dict = bgp_route_maps_route_map_inner_set_instance.to_dict()
# create an instance of BgpRouteMapsRouteMapInnerSet from a dict
bgp_route_maps_route_map_inner_set_from_dict = BgpRouteMapsRouteMapInnerSet.from_dict(bgp_route_maps_route_map_inner_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


