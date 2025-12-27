# HipProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [readonly] 
**match** | **str** |  | 
**name** | **str** | The name of the HIP profile | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_objects.models.hip_profiles import HipProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of HipProfiles from a JSON string
hip_profiles_instance = HipProfiles.from_json(json)
# print the JSON string representation of the object
print(HipProfiles.to_json())

# convert the object into a dict
hip_profiles_dict = hip_profiles_instance.to_dict()
# create an instance of HipProfiles from a dict
hip_profiles_from_dict = HipProfiles.from_dict(hip_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


