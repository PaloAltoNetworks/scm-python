# HaConfigurationsGroupMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_passive** | [**HaConfigurationsGroupModeActivePassive**](HaConfigurationsGroupModeActivePassive.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.ha_configurations_group_mode import HaConfigurationsGroupMode

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupMode from a JSON string
ha_configurations_group_mode_instance = HaConfigurationsGroupMode.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupMode.to_json())

# convert the object into a dict
ha_configurations_group_mode_dict = ha_configurations_group_mode_instance.to_dict()
# create an instance of HaConfigurationsGroupMode from a dict
ha_configurations_group_mode_from_dict = HaConfigurationsGroupMode.from_dict(ha_configurations_group_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


