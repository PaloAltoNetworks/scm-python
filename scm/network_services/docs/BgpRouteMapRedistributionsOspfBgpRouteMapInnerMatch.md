# BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchAddress**](BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchAddress.md) |  | [optional] 
**interface** | **str** | OSPF BGP Route maps Interface | [optional] 
**metric** | **int** | OSPF BGP Route maps Metric | [optional] 
**next_hop** | [**BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchNextHop**](BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatchNextHop.md) |  | [optional] 
**tag** | **int** | OSPF BGP Route maps Tag | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf_bgp_route_map_inner_match import BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatch from a JSON string
bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_instance = BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatch.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatch.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_dict = bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatch from a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_from_dict = BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatch.from_dict(bgp_route_map_redistributions_ospf_bgp_route_map_inner_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


