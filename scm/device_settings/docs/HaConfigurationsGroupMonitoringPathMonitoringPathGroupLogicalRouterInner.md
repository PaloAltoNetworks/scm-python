# HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_ip_group** | [**List[HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInnerDestinationIpGroupInner]**](HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInnerDestinationIpGroupInner.md) |  | [optional] 
**enabled** | **bool** | Enable path group? | [optional] [default to True]
**failure_condition** | **str** | Failure condition | [optional] 
**name** | **str** | Logical router name | 
**ping_count** | **int** | Ping count | [optional] [default to 10]
**ping_interval** | **int** | Ping interval | [optional] [default to 200]

## Example

```python
from scm_device_settings.models.ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner import HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInner

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInner from a JSON string
ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_instance = HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInner.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInner.to_json())

# convert the object into a dict
ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_dict = ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_instance.to_dict()
# create an instance of HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInner from a dict
ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_from_dict = HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInner.from_dict(ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


