# BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4

BGP Root OSPF Route maps match bgp-route-map-redistributions ipv4 object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4Address**](BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4Address.md) |  | [optional] 
**next_hop** | [**BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4NextHop**](BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4NextHop.md) |  | [optional] 
**route_source** | [**BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4RouteSource**](BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4RouteSource.md) |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4 import BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4 from a JSON string
bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_instance = BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_dict = bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4 from a dict
bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_from_dict = BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4.from_dict(bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


