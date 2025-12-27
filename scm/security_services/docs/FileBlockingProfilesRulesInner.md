# FileBlockingProfilesRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to take when the rule match criteria is met | [default to 'alert']
**application** | **List[str]** | The application transferring the files (App-ID naming) | [default to ["any"]]
**direction** | **str** | The direction of the file transfer | [default to 'both']
**file_type** | **List[str]** | The file type | [default to ["any"]]
**name** | **str** | The name of the file blocking rule | 

## Example

```python
from scm_security_services.models.file_blocking_profiles_rules_inner import FileBlockingProfilesRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FileBlockingProfilesRulesInner from a JSON string
file_blocking_profiles_rules_inner_instance = FileBlockingProfilesRulesInner.from_json(json)
# print the JSON string representation of the object
print(FileBlockingProfilesRulesInner.to_json())

# convert the object into a dict
file_blocking_profiles_rules_inner_dict = file_blocking_profiles_rules_inner_instance.to_dict()
# create an instance of FileBlockingProfilesRulesInner from a dict
file_blocking_profiles_rules_inner_from_dict = FileBlockingProfilesRulesInner.from_dict(file_blocking_profiles_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


