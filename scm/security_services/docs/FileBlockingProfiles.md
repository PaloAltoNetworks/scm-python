# FileBlockingProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the file blocking profile | [optional] [readonly] 
**name** | **str** | The name of the file blocking profile | 
**rules** | [**List[FileBlockingProfilesRulesInner]**](FileBlockingProfilesRulesInner.md) | A list of file blocking rules | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_security_services.models.file_blocking_profiles import FileBlockingProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of FileBlockingProfiles from a JSON string
file_blocking_profiles_instance = FileBlockingProfiles.from_json(json)
# print the JSON string representation of the object
print(FileBlockingProfiles.to_json())

# convert the object into a dict
file_blocking_profiles_dict = file_blocking_profiles_instance.to_dict()
# create an instance of FileBlockingProfiles from a dict
file_blocking_profiles_from_dict = FileBlockingProfiles.from_dict(file_blocking_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


