# UpdateScheduleUpdateScheduleThreatsRecurring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**UpdateScheduleUpdateScheduleThreatsRecurringDaily**](UpdateScheduleUpdateScheduleThreatsRecurringDaily.md) |  | [optional] 
**every_30_mins** | [**UpdateScheduleUpdateScheduleThreatsRecurringEvery30Mins**](UpdateScheduleUpdateScheduleThreatsRecurringEvery30Mins.md) |  | [optional] 
**hourly** | [**UpdateScheduleUpdateScheduleThreatsRecurringHourly**](UpdateScheduleUpdateScheduleThreatsRecurringHourly.md) |  | [optional] 
**new_app_threshold** | **int** |  | [optional] 
**var_none** | **object** |  | [optional] 
**sync_to_peer** | **bool** |  | [default to False]
**threshold** | **int** |  | [optional] 
**weekly** | [**UpdateScheduleUpdateScheduleThreatsRecurringWeekly**](UpdateScheduleUpdateScheduleThreatsRecurringWeekly.md) |  | [optional] 

## Example

```python
from scm.device_settings.models.update_schedule_update_schedule_threats_recurring import UpdateScheduleUpdateScheduleThreatsRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleUpdateScheduleThreatsRecurring from a JSON string
update_schedule_update_schedule_threats_recurring_instance = UpdateScheduleUpdateScheduleThreatsRecurring.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleUpdateScheduleThreatsRecurring.to_json())

# convert the object into a dict
update_schedule_update_schedule_threats_recurring_dict = update_schedule_update_schedule_threats_recurring_instance.to_dict()
# create an instance of UpdateScheduleUpdateScheduleThreatsRecurring from a dict
update_schedule_update_schedule_threats_recurring_from_dict = UpdateScheduleUpdateScheduleThreatsRecurring.from_dict(update_schedule_update_schedule_threats_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


