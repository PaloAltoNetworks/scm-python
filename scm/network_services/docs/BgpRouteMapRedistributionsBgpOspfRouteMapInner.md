# BgpRouteMapRedistributionsBgpOspfRouteMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | BGP Root OSPF Route maps Action | [optional] 
**description** | **str** | BGP Root OSPF Route maps Description | [optional] 
**match** | [**BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatch**](BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatch.md) |  | [optional] 
**name** | **int** | BGP Root OSPF Route maps Sequence number | [optional] 
**set** | [**BgpRouteMapRedistributionsBgpOspfRouteMapInnerSet**](BgpRouteMapRedistributionsBgpOspfRouteMapInnerSet.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_route_map_redistributions_bgp_ospf_route_map_inner import BgpRouteMapRedistributionsBgpOspfRouteMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpOspfRouteMapInner from a JSON string
bgp_route_map_redistributions_bgp_ospf_route_map_inner_instance = BgpRouteMapRedistributionsBgpOspfRouteMapInner.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpOspfRouteMapInner.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_ospf_route_map_inner_dict = bgp_route_map_redistributions_bgp_ospf_route_map_inner_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpOspfRouteMapInner from a dict
bgp_route_map_redistributions_bgp_ospf_route_map_inner_from_dict = BgpRouteMapRedistributionsBgpOspfRouteMapInner.from_dict(bgp_route_map_redistributions_bgp_ospf_route_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


