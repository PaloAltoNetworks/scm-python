# BgpRouteMapsRouteMapInnerMatchIpv4

bgp-route-maps ipv4 object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**BgpRouteMapsRouteMapInnerMatchIpv4Address**](BgpRouteMapsRouteMapInnerMatchIpv4Address.md) |  | [optional] 
**next_hop** | [**BgpRouteMapsRouteMapInnerMatchIpv4Address**](BgpRouteMapsRouteMapInnerMatchIpv4Address.md) |  | [optional] 
**route_source** | [**BgpRouteMapsRouteMapInnerMatchIpv4Address**](BgpRouteMapsRouteMapInnerMatchIpv4Address.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_maps_route_map_inner_match_ipv4 import BgpRouteMapsRouteMapInnerMatchIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapsRouteMapInnerMatchIpv4 from a JSON string
bgp_route_maps_route_map_inner_match_ipv4_instance = BgpRouteMapsRouteMapInnerMatchIpv4.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapsRouteMapInnerMatchIpv4.to_json())

# convert the object into a dict
bgp_route_maps_route_map_inner_match_ipv4_dict = bgp_route_maps_route_map_inner_match_ipv4_instance.to_dict()
# create an instance of BgpRouteMapsRouteMapInnerMatchIpv4 from a dict
bgp_route_maps_route_map_inner_match_ipv4_from_dict = BgpRouteMapsRouteMapInnerMatchIpv4.from_dict(bgp_route_maps_route_map_inner_match_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


