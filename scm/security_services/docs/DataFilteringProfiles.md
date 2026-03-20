# DataFilteringProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_capture** | **bool** |  | [optional] 
**description** | **str** | The description of the data filtering profile | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**disable_override** | **str** |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the data filtering profile | [optional] [readonly] 
**name** | **str** | The name of the data filtering profile | [optional] 
**rules** | [**List[DataFilteringProfilesRulesInner]**](DataFilteringProfilesRulesInner.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.security_services.models.data_filtering_profiles import DataFilteringProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of DataFilteringProfiles from a JSON string
data_filtering_profiles_instance = DataFilteringProfiles.from_json(json)
# print the JSON string representation of the object
print(DataFilteringProfiles.to_json())

# convert the object into a dict
data_filtering_profiles_dict = data_filtering_profiles_instance.to_dict()
# create an instance of DataFilteringProfiles from a dict
data_filtering_profiles_from_dict = DataFilteringProfiles.from_dict(data_filtering_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


