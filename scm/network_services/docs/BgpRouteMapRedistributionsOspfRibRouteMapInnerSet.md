# BgpRouteMapRedistributionsOspfRibRouteMapInnerSet

OSPF RIB Route maps set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_address** | **str** | OSPF RIB Route maps set Source address | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf_rib_route_map_inner_set import BgpRouteMapRedistributionsOspfRibRouteMapInnerSet

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfRibRouteMapInnerSet from a JSON string
bgp_route_map_redistributions_ospf_rib_route_map_inner_set_instance = BgpRouteMapRedistributionsOspfRibRouteMapInnerSet.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfRibRouteMapInnerSet.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_rib_route_map_inner_set_dict = bgp_route_map_redistributions_ospf_rib_route_map_inner_set_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfRibRouteMapInnerSet from a dict
bgp_route_map_redistributions_ospf_rib_route_map_inner_set_from_dict = BgpRouteMapRedistributionsOspfRibRouteMapInnerSet.from_dict(bgp_route_map_redistributions_ospf_rib_route_map_inner_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


