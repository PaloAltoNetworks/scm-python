# UpdateScheduleUpdateScheduleWildfireRecurring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**every_15_mins** | [**UpdateScheduleUpdateScheduleWildfireRecurringEvery15Mins**](UpdateScheduleUpdateScheduleWildfireRecurringEvery15Mins.md) |  | [optional] 
**every_30_mins** | [**UpdateScheduleUpdateScheduleWildfireRecurringEvery30Mins**](UpdateScheduleUpdateScheduleWildfireRecurringEvery30Mins.md) |  | [optional] 
**every_hour** | [**UpdateScheduleUpdateScheduleWildfireRecurringEveryHour**](UpdateScheduleUpdateScheduleWildfireRecurringEveryHour.md) |  | [optional] 
**every_min** | [**UpdateScheduleUpdateScheduleWildfireRecurringEveryMin**](UpdateScheduleUpdateScheduleWildfireRecurringEveryMin.md) |  | [optional] 
**var_none** | **object** |  | [optional] 
**real_time** | **object** |  | [optional] 

## Example

```python
from scm.device_settings.models.update_schedule_update_schedule_wildfire_recurring import UpdateScheduleUpdateScheduleWildfireRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleUpdateScheduleWildfireRecurring from a JSON string
update_schedule_update_schedule_wildfire_recurring_instance = UpdateScheduleUpdateScheduleWildfireRecurring.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleUpdateScheduleWildfireRecurring.to_json())

# convert the object into a dict
update_schedule_update_schedule_wildfire_recurring_dict = update_schedule_update_schedule_wildfire_recurring_instance.to_dict()
# create an instance of UpdateScheduleUpdateScheduleWildfireRecurring from a dict
update_schedule_update_schedule_wildfire_recurring_from_dict = UpdateScheduleUpdateScheduleWildfireRecurring.from_dict(update_schedule_update_schedule_wildfire_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


