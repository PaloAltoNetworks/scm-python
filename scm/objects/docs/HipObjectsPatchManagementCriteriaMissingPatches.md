# HipObjectsPatchManagementCriteriaMissingPatches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check** | **str** |  | [default to 'any']
**patches** | **List[str]** |  | [optional] 
**severity** | [**HipObjectsPatchManagementCriteriaMissingPatchesSeverity**](HipObjectsPatchManagementCriteriaMissingPatchesSeverity.md) |  | [optional] 

## Example

```python
from scm.objects.models.hip_objects_patch_management_criteria_missing_patches import HipObjectsPatchManagementCriteriaMissingPatches

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsPatchManagementCriteriaMissingPatches from a JSON string
hip_objects_patch_management_criteria_missing_patches_instance = HipObjectsPatchManagementCriteriaMissingPatches.from_json(json)
# print the JSON string representation of the object
print(HipObjectsPatchManagementCriteriaMissingPatches.to_json())

# convert the object into a dict
hip_objects_patch_management_criteria_missing_patches_dict = hip_objects_patch_management_criteria_missing_patches_instance.to_dict()
# create an instance of HipObjectsPatchManagementCriteriaMissingPatches from a dict
hip_objects_patch_management_criteria_missing_patches_from_dict = HipObjectsPatchManagementCriteriaMissingPatches.from_dict(hip_objects_patch_management_criteria_missing_patches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


