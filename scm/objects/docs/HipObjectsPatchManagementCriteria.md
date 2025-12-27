# HipObjectsPatchManagementCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **str** | is enabled | [optional] 
**is_installed** | **bool** | Is Installed | [optional] [default to True]
**missing_patches** | [**HipObjectsPatchManagementCriteriaMissingPatches**](HipObjectsPatchManagementCriteriaMissingPatches.md) |  | [optional] 

## Example

```python
from scm_objects.models.hip_objects_patch_management_criteria import HipObjectsPatchManagementCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsPatchManagementCriteria from a JSON string
hip_objects_patch_management_criteria_instance = HipObjectsPatchManagementCriteria.from_json(json)
# print the JSON string representation of the object
print(HipObjectsPatchManagementCriteria.to_json())

# convert the object into a dict
hip_objects_patch_management_criteria_dict = hip_objects_patch_management_criteria_instance.to_dict()
# create an instance of HipObjectsPatchManagementCriteria from a dict
hip_objects_patch_management_criteria_from_dict = HipObjectsPatchManagementCriteria.from_dict(hip_objects_patch_management_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


