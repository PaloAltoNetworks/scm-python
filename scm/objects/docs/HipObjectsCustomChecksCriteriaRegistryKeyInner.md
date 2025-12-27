# HipObjectsCustomChecksCriteriaRegistryKeyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value_data** | **str** | Registry key default value data | [optional] 
**name** | **str** | Registry key | 
**negate** | **bool** | Key does not exist or match specified value data | [optional] [default to False]
**registry_value** | [**List[HipObjectsCustomChecksCriteriaRegistryKeyInnerRegistryValueInner]**](HipObjectsCustomChecksCriteriaRegistryKeyInnerRegistryValueInner.md) |  | [optional] 

## Example

```python
from scm.objects.models.hip_objects_custom_checks_criteria_registry_key_inner import HipObjectsCustomChecksCriteriaRegistryKeyInner

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsCustomChecksCriteriaRegistryKeyInner from a JSON string
hip_objects_custom_checks_criteria_registry_key_inner_instance = HipObjectsCustomChecksCriteriaRegistryKeyInner.from_json(json)
# print the JSON string representation of the object
print(HipObjectsCustomChecksCriteriaRegistryKeyInner.to_json())

# convert the object into a dict
hip_objects_custom_checks_criteria_registry_key_inner_dict = hip_objects_custom_checks_criteria_registry_key_inner_instance.to_dict()
# create an instance of HipObjectsCustomChecksCriteriaRegistryKeyInner from a dict
hip_objects_custom_checks_criteria_registry_key_inner_from_dict = HipObjectsCustomChecksCriteriaRegistryKeyInner.from_dict(hip_objects_custom_checks_criteria_registry_key_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


