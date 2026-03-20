# HaConfigurationsGroupStateSynchronization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable session synchronization | [optional] 
**ha2_keep_alive** | [**HaConfigurationsGroupStateSynchronizationHa2KeepAlive**](HaConfigurationsGroupStateSynchronizationHa2KeepAlive.md) |  | [optional] 
**transport** | **str** | Session synchronization transport | [optional] 

## Example

```python
from scm.device_settings.models.ha_configurations_group_state_synchronization import HaConfigurationsGroupStateSynchronization

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupStateSynchronization from a JSON string
ha_configurations_group_state_synchronization_instance = HaConfigurationsGroupStateSynchronization.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupStateSynchronization.to_json())

# convert the object into a dict
ha_configurations_group_state_synchronization_dict = ha_configurations_group_state_synchronization_instance.to_dict()
# create an instance of HaConfigurationsGroupStateSynchronization from a dict
ha_configurations_group_state_synchronization_from_dict = HaConfigurationsGroupStateSynchronization.from_dict(ha_configurations_group_state_synchronization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


