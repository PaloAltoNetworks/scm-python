# HaConfigurationsGroupElectionOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_priority** | **int** | Device priority (1 &#x3D; primary, 2 &#x3D; secondary) | [optional] 
**ha_role** | **str** | Device HA role | [optional] 
**heartbeat_backup** | **bool** |  | [optional] 
**preemptive** | **bool** | Preemption enabled? | [optional] [default to False]

## Example

```python
from scm.device_settings.models.ha_configurations_group_election_option import HaConfigurationsGroupElectionOption

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupElectionOption from a JSON string
ha_configurations_group_election_option_instance = HaConfigurationsGroupElectionOption.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupElectionOption.to_json())

# convert the object into a dict
ha_configurations_group_election_option_dict = ha_configurations_group_election_option_instance.to_dict()
# create an instance of HaConfigurationsGroupElectionOption from a dict
ha_configurations_group_election_option_from_dict = HaConfigurationsGroupElectionOption.from_dict(ha_configurations_group_election_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


