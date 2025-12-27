# BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSet

Connected Static Root OSPF Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSetMetric**](BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSetMetric.md) |  | [optional] 
**metric_type** | **str** | Connected Static BGP OSPF Route map set Metric type | [optional] 
**tag** | **int** | Connected Static BGP OSPF Route map set Tag | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_connected_static_ospf_route_map_inner_set import BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSet

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSet from a JSON string
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_set_instance = BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSet.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSet.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_set_dict = bgp_route_map_redistributions_connected_static_ospf_route_map_inner_set_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSet from a dict
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_set_from_dict = BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSet.from_dict(bgp_route_map_redistributions_connected_static_ospf_route_map_inner_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


