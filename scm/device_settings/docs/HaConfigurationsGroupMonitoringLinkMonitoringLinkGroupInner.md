# HaConfigurationsGroupMonitoringLinkMonitoringLinkGroupInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable link group? | [optional] [default to True]
**failure_condition** | **str** | Failure condition | [optional] 
**interface** | **List[str]** | Interfaces monitored | [optional] 
**name** | **str** | Link group name | 

## Example

```python
from scm.device_settings.models.ha_configurations_group_monitoring_link_monitoring_link_group_inner import HaConfigurationsGroupMonitoringLinkMonitoringLinkGroupInner

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupMonitoringLinkMonitoringLinkGroupInner from a JSON string
ha_configurations_group_monitoring_link_monitoring_link_group_inner_instance = HaConfigurationsGroupMonitoringLinkMonitoringLinkGroupInner.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupMonitoringLinkMonitoringLinkGroupInner.to_json())

# convert the object into a dict
ha_configurations_group_monitoring_link_monitoring_link_group_inner_dict = ha_configurations_group_monitoring_link_monitoring_link_group_inner_instance.to_dict()
# create an instance of HaConfigurationsGroupMonitoringLinkMonitoringLinkGroupInner from a dict
ha_configurations_group_monitoring_link_monitoring_link_group_inner_from_dict = HaConfigurationsGroupMonitoringLinkMonitoringLinkGroupInner.from_dict(ha_configurations_group_monitoring_link_monitoring_link_group_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


