# SchedulesScheduleTypeRecurring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | **List[str]** |  | [optional] 
**weekly** | [**SchedulesScheduleTypeRecurringWeekly**](SchedulesScheduleTypeRecurringWeekly.md) |  | [optional] 

## Example

```python
from scm_objects.models.schedules_schedule_type_recurring import SchedulesScheduleTypeRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulesScheduleTypeRecurring from a JSON string
schedules_schedule_type_recurring_instance = SchedulesScheduleTypeRecurring.from_json(json)
# print the JSON string representation of the object
print(SchedulesScheduleTypeRecurring.to_json())

# convert the object into a dict
schedules_schedule_type_recurring_dict = schedules_schedule_type_recurring_instance.to_dict()
# create an instance of SchedulesScheduleTypeRecurring from a dict
schedules_schedule_type_recurring_from_dict = SchedulesScheduleTypeRecurring.from_dict(schedules_schedule_type_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


