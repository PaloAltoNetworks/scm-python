# BgpRouteMapRedistributionsBgpRibRouteMapInnerSet

Set attributes for BGP route map

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_address** | **str** | BGP Root RIB Route maps set Source address | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_bgp_rib_route_map_inner_set import BgpRouteMapRedistributionsBgpRibRouteMapInnerSet

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInnerSet from a JSON string
bgp_route_map_redistributions_bgp_rib_route_map_inner_set_instance = BgpRouteMapRedistributionsBgpRibRouteMapInnerSet.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpRibRouteMapInnerSet.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_set_dict = bgp_route_map_redistributions_bgp_rib_route_map_inner_set_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInnerSet from a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_set_from_dict = BgpRouteMapRedistributionsBgpRibRouteMapInnerSet.from_dict(bgp_route_map_redistributions_bgp_rib_route_map_inner_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


