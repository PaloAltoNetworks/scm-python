# HaConfigurationsGroupMonitoring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_monitoring** | [**HaConfigurationsGroupMonitoringLinkMonitoring**](HaConfigurationsGroupMonitoringLinkMonitoring.md) |  | [optional] 
**path_monitoring** | [**HaConfigurationsGroupMonitoringPathMonitoring**](HaConfigurationsGroupMonitoringPathMonitoring.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.ha_configurations_group_monitoring import HaConfigurationsGroupMonitoring

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupMonitoring from a JSON string
ha_configurations_group_monitoring_instance = HaConfigurationsGroupMonitoring.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupMonitoring.to_json())

# convert the object into a dict
ha_configurations_group_monitoring_dict = ha_configurations_group_monitoring_instance.to_dict()
# create an instance of HaConfigurationsGroupMonitoring from a dict
ha_configurations_group_monitoring_from_dict = HaConfigurationsGroupMonitoring.from_dict(ha_configurations_group_monitoring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


