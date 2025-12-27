# BgpRouteMapRedistributionsBgpRib

BGP Root RIB

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_map** | [**List[BgpRouteMapRedistributionsBgpRibRouteMapInner]**](BgpRouteMapRedistributionsBgpRibRouteMapInner.md) | BGP Root RIB Route maps | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_bgp_rib import BgpRouteMapRedistributionsBgpRib

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpRib from a JSON string
bgp_route_map_redistributions_bgp_rib_instance = BgpRouteMapRedistributionsBgpRib.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpRib.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_rib_dict = bgp_route_map_redistributions_bgp_rib_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpRib from a dict
bgp_route_map_redistributions_bgp_rib_from_dict = BgpRouteMapRedistributionsBgpRib.from_dict(bgp_route_map_redistributions_bgp_rib_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


