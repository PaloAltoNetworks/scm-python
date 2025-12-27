# BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Connected Static BGP OSPF Route map Action | [optional] 
**description** | **str** | Connected Static BGP OSPF Route map Description | [optional] 
**match** | [**BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatch**](BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerMatch.md) |  | [optional] 
**name** | **int** | Connected Static BGP OSPF Route map Sequence number | [optional] 
**set** | [**BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSet**](BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInnerSet.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_connected_static_ospf_route_map_inner import BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInner from a JSON string
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_instance = BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInner.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInner.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_dict = bgp_route_map_redistributions_connected_static_ospf_route_map_inner_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInner from a dict
bgp_route_map_redistributions_connected_static_ospf_route_map_inner_from_dict = BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInner.from_dict(bgp_route_map_redistributions_connected_static_ospf_route_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


