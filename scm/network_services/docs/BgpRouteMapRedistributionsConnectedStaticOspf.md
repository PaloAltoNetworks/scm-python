# BgpRouteMapRedistributionsConnectedStaticOspf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_map** | [**List[BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInner]**](BgpRouteMapRedistributionsConnectedStaticOspfRouteMapInner.md) | Connected Static  BGP OSPF Route maps | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_connected_static_ospf import BgpRouteMapRedistributionsConnectedStaticOspf

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsConnectedStaticOspf from a JSON string
bgp_route_map_redistributions_connected_static_ospf_instance = BgpRouteMapRedistributionsConnectedStaticOspf.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsConnectedStaticOspf.to_json())

# convert the object into a dict
bgp_route_map_redistributions_connected_static_ospf_dict = bgp_route_map_redistributions_connected_static_ospf_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsConnectedStaticOspf from a dict
bgp_route_map_redistributions_connected_static_ospf_from_dict = BgpRouteMapRedistributionsConnectedStaticOspf.from_dict(bgp_route_map_redistributions_connected_static_ospf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


