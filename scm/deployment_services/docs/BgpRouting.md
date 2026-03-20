# BgpRouting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_route_over_sc** | **bool** |  | [optional] 
**add_host_route_to_ike_peer** | **bool** |  | [optional] 
**backbone_routing** | **str** |  | [optional] 
**outbound_routes_for_services** | **List[str]** |  | [optional] 
**routing_preference** | [**BgpRoutingRoutingPreference**](BgpRoutingRoutingPreference.md) |  | [optional] 
**withdraw_static_route** | **bool** |  | [optional] 

## Example

```python
from scm.deployment_services.models.bgp_routing import BgpRouting

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRouting from a JSON string
bgp_routing_instance = BgpRouting.from_json(json)
# print the JSON string representation of the object
print(BgpRouting.to_json())

# convert the object into a dict
bgp_routing_dict = bgp_routing_instance.to_dict()
# create an instance of BgpRouting from a dict
bgp_routing_from_dict = BgpRouting.from_dict(bgp_routing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


