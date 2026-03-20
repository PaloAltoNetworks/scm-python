# BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4

BGP Route Map Redistributions Root BGP rib Route Map IPv4

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4Address**](BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4Address.md) |  | [optional] 
**next_hop** | [**BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4NextHop**](BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4NextHop.md) |  | [optional] 
**route_source** | [**BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4RouteSource**](BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4RouteSource.md) |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4 import BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4 from a JSON string
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_instance = BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_dict = bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4 from a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_from_dict = BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4.from_dict(bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


