# HipObjectsHostInfoCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_version** | [**HipObjectsHostInfoCriteriaClientVersion**](HipObjectsHostInfoCriteriaClientVersion.md) |  | [optional] 
**domain** | [**HipObjectsHostInfoCriteriaClientVersion**](HipObjectsHostInfoCriteriaClientVersion.md) |  | [optional] 
**host_id** | [**HipObjectsHostInfoCriteriaClientVersion**](HipObjectsHostInfoCriteriaClientVersion.md) |  | [optional] 
**host_name** | [**HipObjectsHostInfoCriteriaClientVersion**](HipObjectsHostInfoCriteriaClientVersion.md) |  | [optional] 
**managed** | **bool** | If device is managed | [optional] 
**os** | [**HipObjectsHostInfoCriteriaOs**](HipObjectsHostInfoCriteriaOs.md) |  | [optional] 
**serial_number** | [**HipObjectsHostInfoCriteriaClientVersion**](HipObjectsHostInfoCriteriaClientVersion.md) |  | [optional] 

## Example

```python
from scm_objects.models.hip_objects_host_info_criteria import HipObjectsHostInfoCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsHostInfoCriteria from a JSON string
hip_objects_host_info_criteria_instance = HipObjectsHostInfoCriteria.from_json(json)
# print the JSON string representation of the object
print(HipObjectsHostInfoCriteria.to_json())

# convert the object into a dict
hip_objects_host_info_criteria_dict = hip_objects_host_info_criteria_instance.to_dict()
# create an instance of HipObjectsHostInfoCriteria from a dict
hip_objects_host_info_criteria_from_dict = HipObjectsHostInfoCriteria.from_dict(hip_objects_host_info_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


