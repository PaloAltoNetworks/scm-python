# HaConfigurationsGroupMonitoringLinkMonitoring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable link monitoring | [optional] [default to False]
**failure_condition** | **str** | Failure condition | [optional] 
**link_group** | [**List[HaConfigurationsGroupMonitoringLinkMonitoringLinkGroupInner]**](HaConfigurationsGroupMonitoringLinkMonitoringLinkGroupInner.md) | Link groups | [optional] 

## Example

```python
from scm.device_settings.models.ha_configurations_group_monitoring_link_monitoring import HaConfigurationsGroupMonitoringLinkMonitoring

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupMonitoringLinkMonitoring from a JSON string
ha_configurations_group_monitoring_link_monitoring_instance = HaConfigurationsGroupMonitoringLinkMonitoring.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupMonitoringLinkMonitoring.to_json())

# convert the object into a dict
ha_configurations_group_monitoring_link_monitoring_dict = ha_configurations_group_monitoring_link_monitoring_instance.to_dict()
# create an instance of HaConfigurationsGroupMonitoringLinkMonitoring from a dict
ha_configurations_group_monitoring_link_monitoring_from_dict = HaConfigurationsGroupMonitoringLinkMonitoring.from_dict(ha_configurations_group_monitoring_link_monitoring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


