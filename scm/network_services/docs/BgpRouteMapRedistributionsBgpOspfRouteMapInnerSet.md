# BgpRouteMapRedistributionsBgpOspfRouteMapInnerSet

BGP Root OSPF Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**BgpRouteMapRedistributionsBgpOspfRouteMapInnerSetMetric**](BgpRouteMapRedistributionsBgpOspfRouteMapInnerSetMetric.md) |  | [optional] 
**metric_type** | **str** | BGP Root OSPF Route maps set Metric type | [optional] 
**tag** | **int** | BGP Root OSPF Route maps set Tag | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_bgp_ospf_route_map_inner_set import BgpRouteMapRedistributionsBgpOspfRouteMapInnerSet

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpOspfRouteMapInnerSet from a JSON string
bgp_route_map_redistributions_bgp_ospf_route_map_inner_set_instance = BgpRouteMapRedistributionsBgpOspfRouteMapInnerSet.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpOspfRouteMapInnerSet.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_ospf_route_map_inner_set_dict = bgp_route_map_redistributions_bgp_ospf_route_map_inner_set_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpOspfRouteMapInnerSet from a dict
bgp_route_map_redistributions_bgp_ospf_route_map_inner_set_from_dict = BgpRouteMapRedistributionsBgpOspfRouteMapInnerSet.from_dict(bgp_route_map_redistributions_bgp_ospf_route_map_inner_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


