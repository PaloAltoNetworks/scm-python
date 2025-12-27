# HipObjectsDataLossPreventionCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **str** | is enabled | [optional] 
**is_installed** | **bool** | Is Installed | [optional] [default to True]

## Example

```python
from scm_objects.models.hip_objects_data_loss_prevention_criteria import HipObjectsDataLossPreventionCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsDataLossPreventionCriteria from a JSON string
hip_objects_data_loss_prevention_criteria_instance = HipObjectsDataLossPreventionCriteria.from_json(json)
# print the JSON string representation of the object
print(HipObjectsDataLossPreventionCriteria.to_json())

# convert the object into a dict
hip_objects_data_loss_prevention_criteria_dict = hip_objects_data_loss_prevention_criteria_instance.to_dict()
# create an instance of HipObjectsDataLossPreventionCriteria from a dict
hip_objects_data_loss_prevention_criteria_from_dict = HipObjectsDataLossPreventionCriteria.from_dict(hip_objects_data_loss_prevention_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


