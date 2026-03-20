# DataFilteringProfilesRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_threshold** | **int** |  | [optional] 
**application** | **List[str]** |  | [optional] 
**block_threshold** | **int** |  | [optional] 
**data_object** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**file_type** | **List[str]** |  | [optional] 
**log_severity** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from scm.security_services.models.data_filtering_profiles_rules_inner import DataFilteringProfilesRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataFilteringProfilesRulesInner from a JSON string
data_filtering_profiles_rules_inner_instance = DataFilteringProfilesRulesInner.from_json(json)
# print the JSON string representation of the object
print(DataFilteringProfilesRulesInner.to_json())

# convert the object into a dict
data_filtering_profiles_rules_inner_dict = data_filtering_profiles_rules_inner_instance.to_dict()
# create an instance of DataFilteringProfilesRulesInner from a dict
data_filtering_profiles_rules_inner_from_dict = DataFilteringProfilesRulesInner.from_dict(data_filtering_profiles_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


