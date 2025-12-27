# BgpRouteMapRedistributionsOspfBgpRouteMapInnerSet

OSPF Root Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregator** | [**BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetAggregator**](BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetAggregator.md) |  | [optional] 
**aspath_prepend** | **List[int]** | OSPF BGP Route maps set AS numbers | [optional] 
**atomic_aggregate** | **bool** | OSPF BGP Route maps set Enable BGP atomic aggregate? | [optional] 
**ipv4** | [**BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetIpv4**](BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetIpv4.md) |  | [optional] 
**large_community** | **List[str]** | OSPF BGP Route maps set Large communities | [optional] 
**local_preference** | **int** | OSPF BGP Route maps set Local preference | [optional] 
**metric** | [**BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetMetric**](BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetMetric.md) |  | [optional] 
**origin** | **str** | OSPF BGP Route maps set Origin | [optional] 
**originator_id** | **str** | OSPF BGP Route maps set Originator ID | [optional] 
**regular_community** | **List[str]** | OSPF BGP Route maps set Regular communities | [optional] 
**tag** | **int** | OSPF BGP Route maps set Tag | [optional] 
**weight** | **int** | OSPF BGP Route maps set Weight | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf_bgp_route_map_inner_set import BgpRouteMapRedistributionsOspfBgpRouteMapInnerSet

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInnerSet from a JSON string
bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_instance = BgpRouteMapRedistributionsOspfBgpRouteMapInnerSet.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfBgpRouteMapInnerSet.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_dict = bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInnerSet from a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_from_dict = BgpRouteMapRedistributionsOspfBgpRouteMapInnerSet.from_dict(bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


