# UpdateScheduleUpdateSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_virus** | [**UpdateScheduleUpdateScheduleAntiVirus**](UpdateScheduleUpdateScheduleAntiVirus.md) |  | 
**threats** | [**UpdateScheduleUpdateScheduleThreats**](UpdateScheduleUpdateScheduleThreats.md) |  | 
**wildfire** | [**UpdateScheduleUpdateScheduleWildfire**](UpdateScheduleUpdateScheduleWildfire.md) |  | 

## Example

```python
from scm_device_settings.models.update_schedule_update_schedule import UpdateScheduleUpdateSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleUpdateSchedule from a JSON string
update_schedule_update_schedule_instance = UpdateScheduleUpdateSchedule.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleUpdateSchedule.to_json())

# convert the object into a dict
update_schedule_update_schedule_dict = update_schedule_update_schedule_instance.to_dict()
# create an instance of UpdateScheduleUpdateSchedule from a dict
update_schedule_update_schedule_from_dict = UpdateScheduleUpdateSchedule.from_dict(update_schedule_update_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


