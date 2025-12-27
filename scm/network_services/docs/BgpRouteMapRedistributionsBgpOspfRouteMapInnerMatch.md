# BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_path_access_list** | **str** | BGP Root OSPF Route maps match AS path access list | [optional] 
**extended_community** | **str** | EBGP Root OSPF Route maps match xtended community | [optional] 
**interface** | **str** | BGP Root OSPF Route maps match Interface | [optional] 
**ipv4** | [**BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4**](BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatchIpv4.md) |  | [optional] 
**large_community** | **str** | BGP Root OSPF Route maps match Large community | [optional] 
**local_preference** | **int** | BGP Root OSPF Route maps match Local preference | [optional] 
**metric** | **int** | BGP Root OSPF Route maps match Metric | [optional] 
**origin** | **str** | BGP Root OSPF Route maps match Origin | [optional] 
**peer** | **str** | BGP Root OSPF Route maps match Peer | [optional] 
**regular_community** | **str** | BGP Root OSPF Route maps match Regular community | [optional] 
**tag** | **int** | BGP Root OSPF Route maps match Tag | [optional] 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_bgp_ospf_route_map_inner_match import BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatch from a JSON string
bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_instance = BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatch.from_json(json)
# print the JSON string representation of the object
print(BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatch.to_json())

# convert the object into a dict
bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_dict = bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_instance.to_dict()
# create an instance of BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatch from a dict
bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_from_dict = BgpRouteMapRedistributionsBgpOspfRouteMapInnerMatch.from_dict(bgp_route_map_redistributions_bgp_ospf_route_map_inner_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


