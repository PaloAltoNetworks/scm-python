# BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchAddress

OSPF RIB Route maps address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_list** | **str** | OSPF RIB Route maps address Access list | [optional] 
**prefix_list** | **str** | OSPF RIB Route maps address Prefix list | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_ospf_rib_route_map_inner_match_address import BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchAddress from a JSON string
bgp_route_map_redistributions_ospf_rib_route_map_inner_match_address_instance = BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchAddress.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchAddress.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_rib_route_map_inner_match_address_dict = bgp_route_map_redistributions_ospf_rib_route_map_inner_match_address_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchAddress from a dict
bgp_route_map_redistributions_ospf_rib_route_map_inner_match_address_from_dict = BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchAddress.from_dict(bgp_route_map_redistributions_ospf_rib_route_map_inner_match_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


