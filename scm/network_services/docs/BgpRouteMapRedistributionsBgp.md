# BgpRouteMapRedistributionsBgp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ospf** | [**BgpRouteMapRedistributionsBgpOspf**](BgpRouteMapRedistributionsBgpOspf.md) |  | [optional] 
**rib** | [**BgpRouteMapRedistributionsBgpRib**](BgpRouteMapRedistributionsBgpRib.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_bgp import BgpRouteMapRedistributionsBgp

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgp from a JSON string
bgp_route_map_redistributions_bgp_instance = BgpRouteMapRedistributionsBgp.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgp.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_dict = bgp_route_map_redistributions_bgp_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgp from a dict
bgp_route_map_redistributions_bgp_from_dict = BgpRouteMapRedistributionsBgp.from_dict(bgp_route_map_redistributions_bgp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


