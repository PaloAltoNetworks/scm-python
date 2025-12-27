# HipObjectsHostInfoCriteriaOsContains


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple** | **str** | Apple vendor | [optional] [default to 'All']
**google** | **str** | Google vendor | [optional] [default to 'All']
**linux** | **str** | Linux vendor | [optional] [default to 'All']
**microsoft** | **str** | Microsoft vendor | [optional] [default to 'All']
**other** | **str** | Other vendor | [optional] 

## Example

```python
from scm_objects.models.hip_objects_host_info_criteria_os_contains import HipObjectsHostInfoCriteriaOsContains

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsHostInfoCriteriaOsContains from a JSON string
hip_objects_host_info_criteria_os_contains_instance = HipObjectsHostInfoCriteriaOsContains.from_json(json)
# print the JSON string representation of the object
print(HipObjectsHostInfoCriteriaOsContains.to_json())

# convert the object into a dict
hip_objects_host_info_criteria_os_contains_dict = hip_objects_host_info_criteria_os_contains_instance.to_dict()
# create an instance of HipObjectsHostInfoCriteriaOsContains from a dict
hip_objects_host_info_criteria_os_contains_from_dict = HipObjectsHostInfoCriteriaOsContains.from_dict(hip_objects_host_info_criteria_os_contains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


