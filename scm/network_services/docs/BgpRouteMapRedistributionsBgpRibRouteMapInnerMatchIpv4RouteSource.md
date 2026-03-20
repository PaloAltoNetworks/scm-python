# BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4RouteSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_list** | **str** | BGP Root RIB Route maps match ipv route source Access list | [optional] 
**prefix_list** | **str** | BGP Root RIB Route maps match ipv route source Prefix list | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_route_source import BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4RouteSource

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4RouteSource from a JSON string
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_route_source_instance = BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4RouteSource.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4RouteSource.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_route_source_dict = bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_route_source_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4RouteSource from a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_route_source_from_dict = BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4RouteSource.from_dict(bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_route_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


