# BgpRoutingRoutingPreference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **object** |  | [optional] 
**hot_potato_routing** | **object** |  | [optional] 

## Example

```python
from scm_deployment_services.models.bgp_routing_routing_preference import BgpRoutingRoutingPreference

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRoutingRoutingPreference from a JSON string
bgp_routing_routing_preference_instance = BgpRoutingRoutingPreference.from_json(json)
# print the JSON string representation of the object
print(BgpRoutingRoutingPreference.to_json())

# convert the object into a dict
bgp_routing_routing_preference_dict = bgp_routing_routing_preference_instance.to_dict()
# create an instance of BgpRoutingRoutingPreference from a dict
bgp_routing_routing_preference_from_dict = BgpRoutingRoutingPreference.from_dict(bgp_routing_routing_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


