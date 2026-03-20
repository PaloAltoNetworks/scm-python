# HipObjectsCustomChecksCriteriaPlistInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**List[HipObjectsCustomChecksCriteriaPlistInnerKeyInner]**](HipObjectsCustomChecksCriteriaPlistInnerKeyInner.md) |  | [optional] 
**name** | **str** | Preference list | 
**negate** | **bool** | Plist does not exist | [optional] [default to False]

## Example

```python
from scm.objects.models.hip_objects_custom_checks_criteria_plist_inner import HipObjectsCustomChecksCriteriaPlistInner

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsCustomChecksCriteriaPlistInner from a JSON string
hip_objects_custom_checks_criteria_plist_inner_instance = HipObjectsCustomChecksCriteriaPlistInner.from_json(json)
# print the JSON string representation of the object
print(HipObjectsCustomChecksCriteriaPlistInner.to_json())

# convert the object into a dict
hip_objects_custom_checks_criteria_plist_inner_dict = hip_objects_custom_checks_criteria_plist_inner_instance.to_dict()
# create an instance of HipObjectsCustomChecksCriteriaPlistInner from a dict
hip_objects_custom_checks_criteria_plist_inner_from_dict = HipObjectsCustomChecksCriteriaPlistInner.from_dict(hip_objects_custom_checks_criteria_plist_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


