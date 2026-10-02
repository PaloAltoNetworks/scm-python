# PbfRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**PbfRulesAction**](PbfRulesAction.md) |  | [optional] 
**application** | **List[str]** | Applications | [optional] 
**description** | **str** | Description | [optional] 
**destination** | **List[str]** | Destination addresses | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**enforce_symmetric_return** | [**PbfRulesEnforceSymmetricReturn**](PbfRulesEnforceSymmetricReturn.md) |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**var_from** | [**PbfRulesFrom**](PbfRulesFrom.md) |  | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | PBF rule name | [optional] 
**negate_destination** | **bool** | Negate destination address | [optional] [default to False]
**negate_source** | **bool** | Negate source address | [optional] [default to False]
**schedule** | **str** | Schedule | [optional] 
**service** | **List[str]** | Services | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**source** | **List[str]** | Source addresses | [optional] 
**source_user** | **List[str]** | Source users | [optional] 
**tag** | **List[str]** | Tags | [optional] 

## Example

```python
from scm.network_services.models.pbf_rules import PbfRules

# TODO update the JSON string below
json = "{}"
# create an instance of PbfRules from a JSON string
pbf_rules_instance = PbfRules.from_json(json)
# print the JSON string representation of the object
print(PbfRules.to_json())

# convert the object into a dict
pbf_rules_dict = pbf_rules_instance.to_dict()
# create an instance of PbfRules from a dict
pbf_rules_from_dict = PbfRules.from_dict(pbf_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


