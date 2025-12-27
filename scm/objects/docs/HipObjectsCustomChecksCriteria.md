# HipObjectsCustomChecksCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plist** | [**List[HipObjectsCustomChecksCriteriaPlistInner]**](HipObjectsCustomChecksCriteriaPlistInner.md) |  | [optional] 
**process_list** | [**List[HipObjectsCustomChecksCriteriaProcessListInner]**](HipObjectsCustomChecksCriteriaProcessListInner.md) |  | [optional] 
**registry_key** | [**List[HipObjectsCustomChecksCriteriaRegistryKeyInner]**](HipObjectsCustomChecksCriteriaRegistryKeyInner.md) |  | [optional] 

## Example

```python
from scm_objects.models.hip_objects_custom_checks_criteria import HipObjectsCustomChecksCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsCustomChecksCriteria from a JSON string
hip_objects_custom_checks_criteria_instance = HipObjectsCustomChecksCriteria.from_json(json)
# print the JSON string representation of the object
print(HipObjectsCustomChecksCriteria.to_json())

# convert the object into a dict
hip_objects_custom_checks_criteria_dict = hip_objects_custom_checks_criteria_instance.to_dict()
# create an instance of HipObjectsCustomChecksCriteria from a dict
hip_objects_custom_checks_criteria_from_dict = HipObjectsCustomChecksCriteria.from_dict(hip_objects_custom_checks_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


