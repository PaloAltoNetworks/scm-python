# HaConfigurationsGroupMonitoringPathMonitoringPathGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_router** | [**List[HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInner]**](HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInner.md) | Logical router | [optional] 

## Example

```python
from scm_device_settings.models.ha_configurations_group_monitoring_path_monitoring_path_group import HaConfigurationsGroupMonitoringPathMonitoringPathGroup

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupMonitoringPathMonitoringPathGroup from a JSON string
ha_configurations_group_monitoring_path_monitoring_path_group_instance = HaConfigurationsGroupMonitoringPathMonitoringPathGroup.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupMonitoringPathMonitoringPathGroup.to_json())

# convert the object into a dict
ha_configurations_group_monitoring_path_monitoring_path_group_dict = ha_configurations_group_monitoring_path_monitoring_path_group_instance.to_dict()
# create an instance of HaConfigurationsGroupMonitoringPathMonitoringPathGroup from a dict
ha_configurations_group_monitoring_path_monitoring_path_group_from_dict = HaConfigurationsGroupMonitoringPathMonitoringPathGroup.from_dict(ha_configurations_group_monitoring_path_monitoring_path_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


