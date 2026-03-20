# BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | Connected Static BGP OSPF Route map Interface | [optional] 
**ipv4** | [**BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4**](BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatchIpv4.md) |  | [optional] 
**metric** | **int** | Connected Static BGP OSPF Route map Metric | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match import BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatch from a JSON string
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_instance = BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatch.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatch.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_dict = bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatch from a dict
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_from_dict = BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatch.from_dict(bgp_route_map_redistributions_connected_static_ospf_route_map_inner_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


