# BgpRouteMapRedistributionsConnectedStaticRibRouteMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Connected Static BGP Rib Route maps Action | [optional] 
**description** | **str** | Connected Static BGP Rib Route maps Description | [optional] 
**match** | [**BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatch**](BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatch.md) |  | [optional] 
**name** | **int** | Connected Static BGP Rib Route maps Sequence number | [optional] 
**set** | [**BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerSet**](BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerSet.md) |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_connected_static_rib_route_map_inner import BgpRouteMapRedistributionsConnectedStaticRibRouteMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticRibRouteMapInner from a JSON string
bgp_route_map_redistributions_connected_static_rib_route_map_inner_instance = BgpRouteMapRedistributionsConnectedStaticRibRouteMapInner.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticRibRouteMapInner.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_rib_route_map_inner_dict = bgp_route_map_redistributions_connected_static_rib_route_map_inner_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticRibRouteMapInner from a dict
bgp_route_map_redistributions_connected_static_rib_route_map_inner_from_dict = BgpRouteMapRedistributionsConnectedStaticRibRouteMapInner.from_dict(bgp_route_map_redistributions_connected_static_rib_route_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


