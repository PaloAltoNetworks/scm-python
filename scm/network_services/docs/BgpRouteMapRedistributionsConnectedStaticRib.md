# BgpRouteMapRedistributionsConnectedStaticRib


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_map** | [**List[BgpRouteMapRedistributionsConnectedStaticRibRouteMapInner]**](BgpRouteMapRedistributionsConnectedStaticRibRouteMapInner.md) | Connected Static BGP Rib Route maps | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_connected_static_rib import BgpRouteMapRedistributionsConnectedStaticRib

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticRib from a JSON string
bgp_route_map_redistributions_connected_static_rib_instance = BgpRouteMapRedistributionsConnectedStaticRib.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticRib.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_rib_dict = bgp_route_map_redistributions_connected_static_rib_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticRib from a dict
bgp_route_map_redistributions_connected_static_rib_from_dict = BgpRouteMapRedistributionsConnectedStaticRib.from_dict(bgp_route_map_redistributions_connected_static_rib_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


