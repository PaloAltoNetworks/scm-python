# BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4NextHop

bgp-route-map-redistributions ipv4 rib object next_hop

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_list** | **str** | BGP Root RIB Route maps match ipv next hop Access list | [optional] 
**prefix_list** | **str** | BGP Root RIB Route maps match ipv next hop Prefix list | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_next_hop import BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4NextHop

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4NextHop from a JSON string
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_next_hop_instance = BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4NextHop.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4NextHop.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_next_hop_dict = bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_next_hop_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4NextHop from a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_next_hop_from_dict = BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4NextHop.from_dict(bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_next_hop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


