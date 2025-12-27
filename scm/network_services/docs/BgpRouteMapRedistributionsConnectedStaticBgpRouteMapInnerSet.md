# BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregator** | [**BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSetAggregator**](BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSetAggregator.md) |  | [optional] 
**aspath_prepend** | **List[int]** | Connected Static BGP Route maps set AS numbers | [optional] 
**atomic_aggregate** | **bool** | Connected Static BGP Route maps set Enable BGP atomic aggregate? | [optional] 
**ipv4** | [**BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSetIpv4**](BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSetIpv4.md) |  | [optional] 
**large_community** | **List[str]** | Connected Static  BGP Route maps set Large communities | [optional] 
**local_preference** | **int** | Connected Static BGP Route maps set Local preference | [optional] 
**metric** | [**BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSetMetric**](BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSetMetric.md) |  | [optional] 
**origin** | **str** | Connected Static BGP Route maps set Origin | [optional] 
**originator_id** | **str** | Connected Static BGP Route maps set Originator ID | [optional] 
**regular_community** | **List[str]** | Connected Static  BGP Route maps set Regular communities | [optional] 
**tag** | **int** | Connected Static BGP Route maps set Tag | [optional] 
**weight** | **int** | Connected Static BGP Route maps set Weight | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_connected_static_bgp_route_map_inner_set import BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSet

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSet from a JSON string
bgp_route_map_redistributions_connected_static_bgp_route_map_inner_set_instance = BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSet.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSet.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_bgp_route_map_inner_set_dict = bgp_route_map_redistributions_connected_static_bgp_route_map_inner_set_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSet from a dict
bgp_route_map_redistributions_connected_static_bgp_route_map_inner_set_from_dict = BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInnerSet.from_dict(bgp_route_map_redistributions_connected_static_bgp_route_map_inner_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


