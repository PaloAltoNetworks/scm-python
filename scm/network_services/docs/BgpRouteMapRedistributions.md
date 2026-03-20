# BgpRouteMapRedistributions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp** | [**BgpRouteMapRedistributionsBgp**](BgpRouteMapRedistributionsBgp.md) |  | [optional] 
**connected_static** | [**BgpRouteMapRedistributionsConnectedStatic**](BgpRouteMapRedistributionsConnectedStatic.md) |  | [optional] 
**description** | **str** | BGP Route Map Redistributions Description | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | BGP Route Map Redistributions UUID of the resource | [optional] [readonly] 
**name** | **str** | BGP Route Map Redistributions Name | 
**ospf** | [**BgpRouteMapRedistributionsOspf**](BgpRouteMapRedistributionsOspf.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions import BgpRouteMapRedistributions

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributions from a JSON string
bgp_route_map_redistributions_instance = BgpRouteMapRedistributions.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributions.to_json())

# convert the object into a dict
bgp_route_map_redistributions_dict = bgp_route_map_redistributions_instance.to_dict()
# create an instance of BgpRouteMapRedistributions from a dict
bgp_route_map_redistributions_from_dict = BgpRouteMapRedistributions.from_dict(bgp_route_map_redistributions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


