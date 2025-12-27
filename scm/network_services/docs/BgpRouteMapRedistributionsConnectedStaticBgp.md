# BgpRouteMapRedistributionsConnectedStaticBgp

Connected Static Root BGP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_map** | [**List[BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInner]**](BgpRouteMapRedistributionsConnectedStaticBgpRouteMapInner.md) | Connected Static BGP Route maps | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_connected_static_bgp import BgpRouteMapRedistributionsConnectedStaticBgp

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticBgp from a JSON string
bgp_route_map_redistributions_connected_static_bgp_instance = BgpRouteMapRedistributionsConnectedStaticBgp.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticBgp.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_bgp_dict = bgp_route_map_redistributions_connected_static_bgp_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticBgp from a dict
bgp_route_map_redistributions_connected_static_bgp_from_dict = BgpRouteMapRedistributionsConnectedStaticBgp.from_dict(bgp_route_map_redistributions_connected_static_bgp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


