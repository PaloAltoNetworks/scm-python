# UpdateScheduleUpdateScheduleAntiVirusRecurring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**UpdateScheduleUpdateScheduleAntiVirusRecurringDaily**](UpdateScheduleUpdateScheduleAntiVirusRecurringDaily.md) |  | [optional] 
**hourly** | [**UpdateScheduleUpdateScheduleAntiVirusRecurringHourly**](UpdateScheduleUpdateScheduleAntiVirusRecurringHourly.md) |  | [optional] 
**var_none** | **object** |  | [optional] 
**sync_to_peer** | **bool** |  | [default to False]
**threshold** | **int** |  | [optional] 
**weekly** | [**UpdateScheduleUpdateScheduleAntiVirusRecurringWeekly**](UpdateScheduleUpdateScheduleAntiVirusRecurringWeekly.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.update_schedule_update_schedule_anti_virus_recurring import UpdateScheduleUpdateScheduleAntiVirusRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleUpdateScheduleAntiVirusRecurring from a JSON string
update_schedule_update_schedule_anti_virus_recurring_instance = UpdateScheduleUpdateScheduleAntiVirusRecurring.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleUpdateScheduleAntiVirusRecurring.to_json())

# convert the object into a dict
update_schedule_update_schedule_anti_virus_recurring_dict = update_schedule_update_schedule_anti_virus_recurring_instance.to_dict()
# create an instance of UpdateScheduleUpdateScheduleAntiVirusRecurring from a dict
update_schedule_update_schedule_anti_virus_recurring_from_dict = UpdateScheduleUpdateScheduleAntiVirusRecurring.from_dict(update_schedule_update_schedule_anti_virus_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


