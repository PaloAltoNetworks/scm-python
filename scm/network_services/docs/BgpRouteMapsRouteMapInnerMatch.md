# BgpRouteMapsRouteMapInnerMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_path_access_list** | **str** | AS path access list | [optional] 
**extended_community** | **str** | Extended community | [optional] 
**interface** | **str** | Interface | [optional] 
**ipv4** | [**BgpRouteMapsRouteMapInnerMatchIpv4**](BgpRouteMapsRouteMapInnerMatchIpv4.md) |  | [optional] 
**large_community** | **str** | Large community | [optional] 
**local_preference** | **int** |  | [optional] 
**metric** | **int** | Metric | [optional] 
**origin** | **str** | Origin | [optional] 
**peer** | **str** | Peer | [optional] 
**regular_community** | **str** | Regular community | [optional] 
**tag** | **int** | Tag | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_maps_route_map_inner_match import BgpRouteMapsRouteMapInnerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapsRouteMapInnerMatch from a JSON string
bgp_route_maps_route_map_inner_match_instance = BgpRouteMapsRouteMapInnerMatch.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapsRouteMapInnerMatch.to_json())

# convert the object into a dict
bgp_route_maps_route_map_inner_match_dict = bgp_route_maps_route_map_inner_match_instance.to_dict()
# create an instance of BgpRouteMapsRouteMapInnerMatch from a dict
bgp_route_maps_route_map_inner_match_from_dict = BgpRouteMapsRouteMapInnerMatch.from_dict(bgp_route_maps_route_map_inner_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


