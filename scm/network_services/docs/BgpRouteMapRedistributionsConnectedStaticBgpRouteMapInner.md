# BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Connected Static BGP Route maps Action | [optional] 
**description** | **str** | Connected Static BGP Route maps Description | [optional] 
**match** | [**BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatch**](BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatch.md) |  | [optional] 
**name** | **int** | Connected Static BGP Route maps Sequence number | [optional] 
**set** | [**BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSet**](BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSet.md) |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_connected_static_bgp_route_map_inner import BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInner from a JSON string
bgp_route_map_redistributions_connected_static_bgp_route_map_inner_instance = BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInner.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInner.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_bgp_route_map_inner_dict = bgp_route_map_redistributions_connected_static_bgp_route_map_inner_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInner from a dict
bgp_route_map_redistributions_connected_static_bgp_route_map_inner_from_dict = BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInner.from_dict(bgp_route_map_redistributions_connected_static_bgp_route_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


