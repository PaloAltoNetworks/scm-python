# PbfRulesActionForwardNexthop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Next hop FQDN | [optional] 
**ip_address** | **str** | Next hop IP address | [optional] 

## Example

```python
from scm.network_services.models.pbf_rules_action_forward_nexthop import PbfRulesActionForwardNexthop

# TODO update the JSON string below
json = "{}"
# create an instance of PbfRulesActionForwardNexthop from a JSON string
pbf_rules_action_forward_nexthop_instance = PbfRulesActionForwardNexthop.from_json(json)
# print the JSON string representation of the object
print(PbfRulesActionForwardNexthop.to_json())

# convert the object into a dict
pbf_rules_action_forward_nexthop_dict = pbf_rules_action_forward_nexthop_instance.to_dict()
# create an instance of PbfRulesActionForwardNexthop from a dict
pbf_rules_action_forward_nexthop_from_dict = PbfRulesActionForwardNexthop.from_dict(pbf_rules_action_forward_nexthop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


