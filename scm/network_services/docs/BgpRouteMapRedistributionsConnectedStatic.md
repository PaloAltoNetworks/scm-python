# BgpRouteMapRedistributionsConnectedStatic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp** | [**BgpRouteMapRedistributionsConnectedStaticBgp**](BgpRouteMapRedistributionsConnectedStaticBgp.md) |  | [optional] 
**ospf** | [**BgpRouteMapRedistributionsConnectedStaticOspf**](BgpRouteMapRedistributionsConnectedStaticOspf.md) |  | [optional] 
**rib** | [**BgpRouteMapRedistributionsConnectedStaticRib**](BgpRouteMapRedistributionsConnectedStaticRib.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_connected_static import BgpRouteMapRedistributionsConnectedStatic

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStatic from a JSON string
bgp_route_map_redistributions_connected_static_instance = BgpRouteMapRedistributionsConnectedStatic.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStatic.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_dict = bgp_route_map_redistributions_connected_static_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStatic from a dict
bgp_route_map_redistributions_connected_static_from_dict = BgpRouteMapRedistributionsConnectedStatic.from_dict(bgp_route_map_redistributions_connected_static_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


