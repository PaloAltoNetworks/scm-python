# BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetAggregator

bgp-route-map-redistributions set aggregator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_as** | **int** | OSPF BGP Route maps set Aggregator AS | [optional] 
**router_id** | **str** | OSPF BGP Route maps set Router ID | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_aggregator import BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetAggregator

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetAggregator from a JSON string
bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_aggregator_instance = BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetAggregator.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetAggregator.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_aggregator_dict = bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_aggregator_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetAggregator from a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_aggregator_from_dict = BgpRouteMapRedistributionsOspfBgpRouteMapInnerSetAggregator.from_dict(bgp_route_map_redistributions_ospf_bgp_route_map_inner_set_aggregator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


