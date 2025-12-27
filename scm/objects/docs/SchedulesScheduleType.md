# SchedulesScheduleType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_recurring** | **List[str]** |  | [optional] 
**recurring** | [**SchedulesScheduleTypeRecurring**](SchedulesScheduleTypeRecurring.md) |  | [optional] 

## Example

```python
from scm.objects.models.schedules_schedule_type import SchedulesScheduleType

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulesScheduleType from a JSON string
schedules_schedule_type_instance = SchedulesScheduleType.from_json(json)
# print the JSON string representation of the object
print(SchedulesScheduleType.to_json())

# convert the object into a dict
schedules_schedule_type_dict = schedules_schedule_type_instance.to_dict()
# create an instance of SchedulesScheduleType from a dict
schedules_schedule_type_from_dict = SchedulesScheduleType.from_dict(schedules_schedule_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


