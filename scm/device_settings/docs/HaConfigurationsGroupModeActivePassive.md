# HaConfigurationsGroupModeActivePassive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_fail_hold_down_time** | **int** | Monitor hold time (milliseconds) | [optional] [default to 3000]
**passive_link_state** | **str** | Passive link state | [optional] 

## Example

```python
from scm.device_settings.models.ha_configurations_group_mode_active_passive import HaConfigurationsGroupModeActivePassive

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupModeActivePassive from a JSON string
ha_configurations_group_mode_active_passive_instance = HaConfigurationsGroupModeActivePassive.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupModeActivePassive.to_json())

# convert the object into a dict
ha_configurations_group_mode_active_passive_dict = ha_configurations_group_mode_active_passive_instance.to_dict()
# create an instance of HaConfigurationsGroupModeActivePassive from a dict
ha_configurations_group_mode_active_passive_from_dict = HaConfigurationsGroupModeActivePassive.from_dict(ha_configurations_group_mode_active_passive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


