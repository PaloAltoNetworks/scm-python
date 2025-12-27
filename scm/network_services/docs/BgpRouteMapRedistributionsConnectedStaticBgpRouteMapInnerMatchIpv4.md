# BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4

bgp-route-map-redistributions connected-static ipv4

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4Address**](BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4Address.md) |  | [optional] 
**next_hop** | [**BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4NextHop**](BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4NextHop.md) |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_connected_static_bgp_route_map_inner_match_ipv4 import BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4 from a JSON string
bgp_route_map_redistributions_connected_static_bgp_route_map_inner_match_ipv4_instance = BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_bgp_route_map_inner_match_ipv4_dict = bgp_route_map_redistributions_connected_static_bgp_route_map_inner_match_ipv4_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4 from a dict
bgp_route_map_redistributions_connected_static_bgp_route_map_inner_match_ipv4_from_dict = BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerMatchIpv4.from_dict(bgp_route_map_redistributions_connected_static_bgp_route_map_inner_match_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


