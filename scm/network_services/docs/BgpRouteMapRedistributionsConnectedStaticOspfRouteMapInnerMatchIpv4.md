# BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4

bgp-route-map-redistributions connected-static match ipv4

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4Address**](BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4Address.md) |  | [optional] 
**next_hop** | [**BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4NextHop**](BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4NextHop.md) |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_ipv4 import BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4 from a JSON string
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_ipv4_instance = BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_ipv4_dict = bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_ipv4_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4 from a dict
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_ipv4_from_dict = BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4.from_dict(bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


