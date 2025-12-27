# BgpRouteMapRedistributionsOspfRibRouteMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | OSPF RIB Route maps Action | [optional] 
**description** | **str** | OSPF RIB Route maps Description | [optional] 
**match** | [**BgpRouteMapRedistributionsOspfRibRouteMapInnerMatch**](BgpRouteMapRedistributionsOspfRibRouteMapInnerMatch.md) |  | [optional] 
**name** | **int** | OSPF RIB Route mapsSequence number | [optional] 
**set** | [**BgpRouteMapRedistributionsOspfRibRouteMapInnerSet**](BgpRouteMapRedistributionsOspfRibRouteMapInnerSet.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf_rib_route_map_inner import BgpRouteMapRedistributionsOspfRibRouteMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfRibRouteMapInner from a JSON string
bgp_route_map_redistributions_ospf_rib_route_map_inner_instance = BgpRouteMapRedistributionsOspfRibRouteMapInner.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfRibRouteMapInner.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_rib_route_map_inner_dict = bgp_route_map_redistributions_ospf_rib_route_map_inner_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfRibRouteMapInner from a dict
bgp_route_map_redistributions_ospf_rib_route_map_inner_from_dict = BgpRouteMapRedistributionsOspfRibRouteMapInner.from_dict(bgp_route_map_redistributions_ospf_rib_route_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


