# PbfRulesFrom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **List[str]** | Source interfaces | [optional] 
**zone** | **List[str]** | Source zones | [optional] 

## Example

```python
from scm.network_services.models.pbf_rules_from import PbfRulesFrom

# TODO update the JSON string below
json = "{}"
# create an instance of PbfRulesFrom from a JSON string
pbf_rules_from_instance = PbfRulesFrom.from_json(json)
# print the JSON string representation of the object
print(PbfRulesFrom.to_json())

# convert the object into a dict
pbf_rules_from_dict = pbf_rules_from_instance.to_dict()
# create an instance of PbfRulesFrom from a dict
pbf_rules_from_from_dict = PbfRulesFrom.from_dict(pbf_rules_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


