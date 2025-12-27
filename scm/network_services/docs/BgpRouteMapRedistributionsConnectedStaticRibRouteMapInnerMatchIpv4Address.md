# BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatchIpv4Address

Connected Static BGP Rib Route maps ipv4 address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_list** | **str** | Connected Static BGP Rib Route maps ipv4 Access list | [optional] 
**prefix_list** | **str** | Connected Static BGP Rib Route maps ipv4 Prefix list | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_ipv4_address import BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatchIpv4Address

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatchIpv4Address from a JSON string
bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_ipv4_address_instance = BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatchIpv4Address.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatchIpv4Address.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_ipv4_address_dict = bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_ipv4_address_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatchIpv4Address from a dict
bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_ipv4_address_from_dict = BgpRouteMapRedistributionsConnectedStaticRibRouteMapInnerMatchIpv4Address.from_dict(bgp_route_map_redistributions_connected_static_rib_route_map_inner_match_ipv4_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


