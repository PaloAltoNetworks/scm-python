# BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchNextHop

bgp-route-map-redistributions ospf next_hop

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_list** | **str** | OSPF BGP Route maps next_hop Access list | [optional] 
**prefix_list** | **str** | OSPF BGP Route maps next_hop Prefix list | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_next_hop import BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchNextHop

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchNextHop from a JSON string
bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_next_hop_instance = BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchNextHop.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchNextHop.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_next_hop_dict = bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_next_hop_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchNextHop from a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_next_hop_from_dict = BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchNextHop.from_dict(bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_next_hop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


