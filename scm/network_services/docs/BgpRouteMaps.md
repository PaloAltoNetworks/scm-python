# BgpRouteMaps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** |  | 
**route_map** | [**List[BgpRouteMapsRouteMapInner]**](BgpRouteMapsRouteMapInner.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_maps import BgpRouteMaps

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMaps from a JSON string
bgp_route_maps_instance = BgpRouteMaps.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMaps.to_json())

# convert the object into a dict
bgp_route_maps_dict = bgp_route_maps_instance.to_dict()
# create an instance of BgpRouteMaps from a dict
bgp_route_maps_from_dict = BgpRouteMaps.from_dict(bgp_route_maps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


