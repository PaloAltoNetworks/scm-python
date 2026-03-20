# HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInnerDestinationIpGroupInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_ip** | **List[str]** | Destination IP addresses | [optional] 
**enabled** | **bool** | Enable destination IP group? | [optional] 
**failure_condition** | **str** | Failure condition | [optional] 
**name** | **str** | Destination IP group name | 

## Example

```python
from scm.device_settings.models.ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_destination_ip_group_inner import HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInnerDestinationIpGroupInner

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInnerDestinationIpGroupInner from a JSON string
ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_destination_ip_group_inner_instance = HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInnerDestinationIpGroupInner.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInnerDestinationIpGroupInner.to_json())

# convert the object into a dict
ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_destination_ip_group_inner_dict = ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_destination_ip_group_inner_instance.to_dict()
# create an instance of HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInnerDestinationIpGroupInner from a dict
ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_destination_ip_group_inner_from_dict = HaConfigurationsGroupMonitoringPathMonitoringPathGroupLogicalRouterInnerDestinationIpGroupInner.from_dict(ha_configurations_group_monitoring_path_monitoring_path_group_logical_router_inner_destination_ip_group_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


