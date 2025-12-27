# HaConfigurationsGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | HA group description (not currently used) | [optional] [default to 'N/A']
**election_option** | [**HaConfigurationsGroupElectionOption**](HaConfigurationsGroupElectionOption.md) |  | 
**group_id** | **int** | HA group ID | 
**mode** | [**HaConfigurationsGroupMode**](HaConfigurationsGroupMode.md) |  | 
**monitoring** | [**HaConfigurationsGroupMonitoring**](HaConfigurationsGroupMonitoring.md) |  | 
**peer_ip** | **str** | Peer HA1 IP address | 
**peer_ip_backup** | **str** | Peer HA1 backup IP address | [optional] 
**peer_serial** | **str** | Serial number of the HA peer | 
**state_synchronization** | [**HaConfigurationsGroupStateSynchronization**](HaConfigurationsGroupStateSynchronization.md) |  | 

## Example

```python
from scm_device_settings.models.ha_configurations_group import HaConfigurationsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroup from a JSON string
ha_configurations_group_instance = HaConfigurationsGroup.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroup.to_json())

# convert the object into a dict
ha_configurations_group_dict = ha_configurations_group_instance.to_dict()
# create an instance of HaConfigurationsGroup from a dict
ha_configurations_group_from_dict = HaConfigurationsGroup.from_dict(ha_configurations_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


