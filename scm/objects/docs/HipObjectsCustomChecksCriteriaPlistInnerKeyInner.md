# HipObjectsCustomChecksCriteriaPlistInnerKeyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Key name | 
**negate** | **bool** | Value does not exist or match specified value data | [optional] [default to False]
**value** | **str** | Key value | [optional] 

## Example

```python
from scm_objects.models.hip_objects_custom_checks_criteria_plist_inner_key_inner import HipObjectsCustomChecksCriteriaPlistInnerKeyInner

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsCustomChecksCriteriaPlistInnerKeyInner from a JSON string
hip_objects_custom_checks_criteria_plist_inner_key_inner_instance = HipObjectsCustomChecksCriteriaPlistInnerKeyInner.from_json(json)
# print the JSON string representation of the object
print(HipObjectsCustomChecksCriteriaPlistInnerKeyInner.to_json())

# convert the object into a dict
hip_objects_custom_checks_criteria_plist_inner_key_inner_dict = hip_objects_custom_checks_criteria_plist_inner_key_inner_instance.to_dict()
# create an instance of HipObjectsCustomChecksCriteriaPlistInnerKeyInner from a dict
hip_objects_custom_checks_criteria_plist_inner_key_inner_from_dict = HipObjectsCustomChecksCriteriaPlistInnerKeyInner.from_dict(hip_objects_custom_checks_criteria_plist_inner_key_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


