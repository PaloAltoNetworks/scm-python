# Schedules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the schedule | [readonly] 
**name** | **str** | The name of the schedule | 
**schedule_type** | [**SchedulesScheduleType**](SchedulesScheduleType.md) |  | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_objects.models.schedules import Schedules

# TODO update the JSON string below
json = "{}"
# create an instance of Schedules from a JSON string
schedules_instance = Schedules.from_json(json)
# print the JSON string representation of the object
print(Schedules.to_json())

# convert the object into a dict
schedules_dict = schedules_instance.to_dict()
# create an instance of Schedules from a dict
schedules_from_dict = Schedules.from_dict(schedules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


