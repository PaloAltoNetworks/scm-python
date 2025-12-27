# BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchAddress

bgp-route-map-redistributions ospf address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_list** | **str** | OSPF BGP Route maps match Access list | [optional] 
**prefix_list** | **str** | OSPF BGP Route maps match Prefix list | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_address import BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchAddress from a JSON string
bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_address_instance = BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchAddress.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchAddress.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_address_dict = bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_address_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchAddress from a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_address_from_dict = BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchAddress.from_dict(bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


