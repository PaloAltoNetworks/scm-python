# BgpRouteMapRedistributionsOspfRibRouteMapInnerMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchAddress**](BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchAddress.md) |  | [optional] 
**interface** | **str** | OSPF RIB Route maps Interface | [optional] 
**metric** | **int** | OSPF RIB Route maps Metric | [optional] 
**next_hop** | [**BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchNextHop**](BgpRouteMapRedistributionsOspfRibRouteMapInnerMatchNextHop.md) |  | [optional] 
**tag** | **int** | OSPF RIB Route maps tag | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf_rib_route_map_inner_match import BgpRouteMapRedistributionsOspfRibRouteMapInnerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfRibRouteMapInnerMatch from a JSON string
bgp_route_map_redistributions_ospf_rib_route_map_inner_match_instance = BgpRouteMapRedistributionsOspfRibRouteMapInnerMatch.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfRibRouteMapInnerMatch.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_rib_route_map_inner_match_dict = bgp_route_map_redistributions_ospf_rib_route_map_inner_match_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfRibRouteMapInnerMatch from a dict
bgp_route_map_redistributions_ospf_rib_route_map_inner_match_from_dict = BgpRouteMapRedistributionsOspfRibRouteMapInnerMatch.from_dict(bgp_route_map_redistributions_ospf_rib_route_map_inner_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


