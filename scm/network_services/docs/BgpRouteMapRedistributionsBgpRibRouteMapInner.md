# BgpRouteMapRedistributionsBgpRibRouteMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | BGP Root RIB Route maps Action | [optional] 
**description** | **str** | BGP Root RIB Route maps Description | [optional] 
**match** | [**BgpRouteMapRedistributionsBgpRibRouteMapInnerMatch**](BgpRouteMapRedistributionsBgpRibRouteMapInnerMatch.md) |  | [optional] 
**name** | **int** | BGP Root RIB Route maps Sequence number | [optional] 
**set** | [**BgpRouteMapRedistributionsBgpRibRouteMapInnerSet**](BgpRouteMapRedistributionsBgpRibRouteMapInnerSet.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_bgp_rib_route_map_inner import BgpRouteMapRedistributionsBgpRibRouteMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInner from a JSON string
bgp_route_map_redistributions_bgp_rib_route_map_inner_instance = BgpRouteMapRedistributionsBgpRibRouteMapInner.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpRibRouteMapInner.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_dict = bgp_route_map_redistributions_bgp_rib_route_map_inner_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpRibRouteMapInner from a dict
bgp_route_map_redistributions_bgp_rib_route_map_inner_from_dict = BgpRouteMapRedistributionsBgpRibRouteMapInner.from_dict(bgp_route_map_redistributions_bgp_rib_route_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


