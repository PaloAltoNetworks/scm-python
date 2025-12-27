# BgpRouteMapRedistributionsBgpOspf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_map** | [**List[BgpRouteMapRedistributionsBgpOspfRouteMapInner]**](BgpRouteMapRedistributionsBgpOspfRouteMapInner.md) | BGP Root OSPF Route maps | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_bgp_ospf import BgpRouteMapRedistributionsBgpOspf

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpOspf from a JSON string
bgp_route_map_redistributions_bgp_ospf_instance = BgpRouteMapRedistributionsBgpOspf.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpOspf.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_ospf_dict = bgp_route_map_redistributions_bgp_ospf_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpOspf from a dict
bgp_route_map_redistributions_bgp_ospf_from_dict = BgpRouteMapRedistributionsBgpOspf.from_dict(bgp_route_map_redistributions_bgp_ospf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


