# SchedulesScheduleTypeRecurringWeekly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friday** | **List[str]** |  | [optional] 
**monday** | **List[str]** |  | [optional] 
**saturday** | **List[str]** |  | [optional] 
**sunday** | **List[str]** |  | [optional] 
**thursday** | **List[str]** |  | [optional] 
**tuesday** | **List[str]** |  | [optional] 
**wednesday** | **List[str]** |  | [optional] 

## Example

```python
from scm_objects.models.schedules_schedule_type_recurring_weekly import SchedulesScheduleTypeRecurringWeekly

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulesScheduleTypeRecurringWeekly from a JSON string
schedules_schedule_type_recurring_weekly_instance = SchedulesScheduleTypeRecurringWeekly.from_json(json)
# print the JSON string representation of the object
print(SchedulesScheduleTypeRecurringWeekly.to_json())

# convert the object into a dict
schedules_schedule_type_recurring_weekly_dict = schedules_schedule_type_recurring_weekly_instance.to_dict()
# create an instance of SchedulesScheduleTypeRecurringWeekly from a dict
schedules_schedule_type_recurring_weekly_from_dict = SchedulesScheduleTypeRecurringWeekly.from_dict(schedules_schedule_type_recurring_weekly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


