# UpdateSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**update_schedule** | [**UpdateScheduleUpdateSchedule**](UpdateScheduleUpdateSchedule.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.update_schedule import UpdateSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSchedule from a JSON string
update_schedule_instance = UpdateSchedule.from_json(json)
# print the JSON string representation of the object
print(UpdateSchedule.to_json())

# convert the object into a dict
update_schedule_dict = update_schedule_instance.to_dict()
# create an instance of UpdateSchedule from a dict
update_schedule_from_dict = UpdateSchedule.from_dict(update_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


