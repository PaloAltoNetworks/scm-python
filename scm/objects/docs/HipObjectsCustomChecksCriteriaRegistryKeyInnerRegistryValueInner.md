# HipObjectsCustomChecksCriteriaRegistryKeyInnerRegistryValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Registry value name | 
**negate** | **bool** | Value does not exist or match specified value data | [optional] [default to False]
**value_data** | **str** | Registry value data | [optional] 

## Example

```python
from scm.objects.models.hip_objects_custom_checks_criteria_registry_key_inner_registry_value_inner import HipObjectsCustomChecksCriteriaRegistryKeyInnerRegistryValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsCustomChecksCriteriaRegistryKeyInnerRegistryValueInner from a JSON string
hip_objects_custom_checks_criteria_registry_key_inner_registry_value_inner_instance = HipObjectsCustomChecksCriteriaRegistryKeyInnerRegistryValueInner.from_json(json)
# print the JSON string representation of the object
print(HipObjectsCustomChecksCriteriaRegistryKeyInnerRegistryValueInner.to_json())

# convert the object into a dict
hip_objects_custom_checks_criteria_registry_key_inner_registry_value_inner_dict = hip_objects_custom_checks_criteria_registry_key_inner_registry_value_inner_instance.to_dict()
# create an instance of HipObjectsCustomChecksCriteriaRegistryKeyInnerRegistryValueInner from a dict
hip_objects_custom_checks_criteria_registry_key_inner_registry_value_inner_from_dict = HipObjectsCustomChecksCriteriaRegistryKeyInnerRegistryValueInner.from_dict(hip_objects_custom_checks_criteria_registry_key_inner_registry_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


