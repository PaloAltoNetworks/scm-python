# HipObjectsPatchManagement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | [**HipObjectsPatchManagementCriteria**](HipObjectsPatchManagementCriteria.md) |  | [optional] 
**exclude_vendor** | **bool** |  | [optional] [default to False]
**vendor** | [**List[HipObjectsDataLossPreventionVendorInner]**](HipObjectsDataLossPreventionVendorInner.md) | Vendor name | [optional] 

## Example

```python
from scm.objects.models.hip_objects_patch_management import HipObjectsPatchManagement

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsPatchManagement from a JSON string
hip_objects_patch_management_instance = HipObjectsPatchManagement.from_json(json)
# print the JSON string representation of the object
print(HipObjectsPatchManagement.to_json())

# convert the object into a dict
hip_objects_patch_management_dict = hip_objects_patch_management_instance.to_dict()
# create an instance of HipObjectsPatchManagement from a dict
hip_objects_patch_management_from_dict = HipObjectsPatchManagement.from_dict(hip_objects_patch_management_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


