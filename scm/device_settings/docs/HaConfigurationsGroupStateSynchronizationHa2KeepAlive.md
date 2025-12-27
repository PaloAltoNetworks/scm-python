# HaConfigurationsGroupStateSynchronizationHa2KeepAlive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Keep-alive action | [optional] 
**enabled** | **bool** | Enable HA2 keep-alives? | [optional] [default to False]
**threshold** | **int** | Keep-alive threshold (milliseconds) | [optional] [default to 10000]

## Example

```python
from scm_device_settings.models.ha_configurations_group_state_synchronization_ha2_keep_alive import HaConfigurationsGroupStateSynchronizationHa2KeepAlive

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupStateSynchronizationHa2KeepAlive from a JSON string
ha_configurations_group_state_synchronization_ha2_keep_alive_instance = HaConfigurationsGroupStateSynchronizationHa2KeepAlive.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupStateSynchronizationHa2KeepAlive.to_json())

# convert the object into a dict
ha_configurations_group_state_synchronization_ha2_keep_alive_dict = ha_configurations_group_state_synchronization_ha2_keep_alive_instance.to_dict()
# create an instance of HaConfigurationsGroupStateSynchronizationHa2KeepAlive from a dict
ha_configurations_group_state_synchronization_ha2_keep_alive_from_dict = HaConfigurationsGroupStateSynchronizationHa2KeepAlive.from_dict(ha_configurations_group_state_synchronization_ha2_keep_alive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


