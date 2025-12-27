# BgpRouteMapRedistributionsOspfRib


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_map** | [**List[BgpRouteMapRedistributionsOspfRibRouteMapInner]**](BgpRouteMapRedistributionsOspfRibRouteMapInner.md) | OSPF RIB Route maps set Route maps | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf_rib import BgpRouteMapRedistributionsOspfRib

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspfRib from a JSON string
bgp_route_map_redistributions_ospf_rib_instance = BgpRouteMapRedistributionsOspfRib.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspfRib.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_rib_dict = bgp_route_map_redistributions_ospf_rib_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspfRib from a dict
bgp_route_map_redistributions_ospf_rib_from_dict = BgpRouteMapRedistributionsOspfRib.from_dict(bgp_route_map_redistributions_ospf_rib_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


