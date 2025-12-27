# HipObjectsMobileDeviceCriteriaLastCheckinTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_within** | [**HipObjectsMobileDeviceCriteriaLastCheckinTimeNotWithin**](HipObjectsMobileDeviceCriteriaLastCheckinTimeNotWithin.md) |  | [optional] 
**within** | [**HipObjectsMobileDeviceCriteriaLastCheckinTimeNotWithin**](HipObjectsMobileDeviceCriteriaLastCheckinTimeNotWithin.md) |  | [optional] 

## Example

```python
from scm_objects.models.hip_objects_mobile_device_criteria_last_checkin_time import HipObjectsMobileDeviceCriteriaLastCheckinTime

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsMobileDeviceCriteriaLastCheckinTime from a JSON string
hip_objects_mobile_device_criteria_last_checkin_time_instance = HipObjectsMobileDeviceCriteriaLastCheckinTime.from_json(json)
# print the JSON string representation of the object
print(HipObjectsMobileDeviceCriteriaLastCheckinTime.to_json())

# convert the object into a dict
hip_objects_mobile_device_criteria_last_checkin_time_dict = hip_objects_mobile_device_criteria_last_checkin_time_instance.to_dict()
# create an instance of HipObjectsMobileDeviceCriteriaLastCheckinTime from a dict
hip_objects_mobile_device_criteria_last_checkin_time_from_dict = HipObjectsMobileDeviceCriteriaLastCheckinTime.from_dict(hip_objects_mobile_device_criteria_last_checkin_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


