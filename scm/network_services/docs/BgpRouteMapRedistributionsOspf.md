# BgpRouteMapRedistributionsOspf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp** | [**BgpRouteMapRedistributionsOspfBgp**](BgpRouteMapRedistributionsOspfBgp.md) |  | [optional] 
**rib** | [**BgpRouteMapRedistributionsOspfRib**](BgpRouteMapRedistributionsOspfRib.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_ospf import BgpRouteMapRedistributionsOspf

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsOspf from a JSON string
bgp_route_map_redistributions_ospf_instance = BgpRouteMapRedistributionsOspf.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsOspf.to_json())

# convert the object into a dict
bgp_route_map_redistributions_ospf_dict = bgp_route_map_redistributions_ospf_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsOspf from a dict
bgp_route_map_redistributions_ospf_from_dict = BgpRouteMapRedistributionsOspf.from_dict(bgp_route_map_redistributions_ospf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


