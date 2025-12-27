# BgpRouteMapRedistributionsOspfBgpRouteMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | OSPF BGP Route maps Action | [optional] 
**description** | **str** | OSPF BGP Route maps Description | [optional] 
**match** | [**BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatch**](BgpRouteMapRedistributionsOspfBgpRouteMapInnerMatch.md) |  | [optional] 
**name** | **int** | OSPF BGP Route maps Sequence number | [optional] 
**set** | [**BgpRouteMapRedistributionsOspfBgpRouteMapInnerSet**](BgpRouteMapRedistributionsOspfBgpRouteMapInnerSet.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf_bgp_route_map_inner import BgpRouteMapRedistributionsOspfBgpRouteMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInner from a JSON string
bgp_route_map_redistributions_ospf_bgp_route_map_inner_instance = BgpRouteMapRedistributionsOspfBgpRouteMapInner.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfBgpRouteMapInner.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_dict = bgp_route_map_redistributions_ospf_bgp_route_map_inner_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfBgpRouteMapInner from a dict
bgp_route_map_redistributions_ospf_bgp_route_map_inner_from_dict = BgpRouteMapRedistributionsOspfBgpRouteMapInner.from_dict(bgp_route_map_redistributions_ospf_bgp_route_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


