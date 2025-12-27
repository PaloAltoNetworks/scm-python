# BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4Address

bgp-route-map-redistributions ipv4 rib object address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_list** | **str** | BGP Root RIB Route maps match ipv Access list | [optional] 
**prefix_list** | **str** | BGP Root RIB Route maps match ipv Prefix list | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_address import BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4Address

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4Address from a JSON string
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_address_instance = BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4Address.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4Address.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_address_dict = bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_address_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4Address from a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_address_from_dict = BgpRouteMapRedistributionsBgpRibRouteMapInnerMatchIpv4Address.from_dict(bgp_route_map_redistributions_bgp_rib_route_map_inner_match_ipv4_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


