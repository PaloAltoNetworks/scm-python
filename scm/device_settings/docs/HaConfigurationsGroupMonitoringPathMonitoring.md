# HaConfigurationsGroupMonitoringPathMonitoring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable path monitoring? | [optional] [default to False]
**failure_condition** | **str** |  | [optional] 
**path_group** | [**HaConfigurationsGroupMonitoringPathMonitoringPathGroup**](HaConfigurationsGroupMonitoringPathMonitoringPathGroup.md) |  | [optional] 

## Example

```python
from scm.device_settings.models.ha_configurations_group_monitoring_path_monitoring import HaConfigurationsGroupMonitoringPathMonitoring

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupMonitoringPathMonitoring from a JSON string
ha_configurations_group_monitoring_path_monitoring_instance = HaConfigurationsGroupMonitoringPathMonitoring.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupMonitoringPathMonitoring.to_json())

# convert the object into a dict
ha_configurations_group_monitoring_path_monitoring_dict = ha_configurations_group_monitoring_path_monitoring_instance.to_dict()
# create an instance of HaConfigurationsGroupMonitoringPathMonitoring from a dict
ha_configurations_group_monitoring_path_monitoring_from_dict = HaConfigurationsGroupMonitoringPathMonitoring.from_dict(ha_configurations_group_monitoring_path_monitoring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


