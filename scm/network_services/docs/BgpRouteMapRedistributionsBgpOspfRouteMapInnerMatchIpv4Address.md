# BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4Address

BGP Root OSPF Route maps match bgp-route-map-redistributions ipv4 object address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_list** | **str** | BGP Root OSPF Route maps match ipv4 Access list | [optional] 
**prefix_list** | **str** | BGP Root OSPF Route maps match ipv4 Prefix list | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_address import BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4Address

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4Address from a JSON string
bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_address_instance = BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4Address.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4Address.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_address_dict = bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_address_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4Address from a dict
bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_address_from_dict = BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4Address.from_dict(bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_ipv4_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


