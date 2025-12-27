# BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | Connected Static BGP Rib Route maps Interface | [optional] 
**ipv4** | [**BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatchIpv4**](BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatchIpv4.md) |  | [optional] 
**metric** | **int** | Connected Static BGP Rib Route maps Metric | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_connected_static_rib_route_map_inner_match import BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatch from a JSON string
bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_instance = BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatch.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatch.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_dict = bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatch from a dict
bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_from_dict = BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatch.from_dict(bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


