# HaConfigurationsInterfaceHa1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | HA1 default gateway | [optional] 
**ip_address** | **str** | HA1 IP address | [optional] 
**monitor_hold_time** | **int** | HA1 monitor hold time | [default to 3000]
**netmask** | **str** | HA1 netmask | [optional] 
**port** | **str** | HA1 port | 

## Example

```python
from scm.device_settings.models.ha_configurations_interface_ha1 import HaConfigurationsInterfaceHa1

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsInterfaceHa1 from a JSON string
ha_configurations_interface_ha1_instance = HaConfigurationsInterfaceHa1.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsInterfaceHa1.to_json())

# convert the object into a dict
ha_configurations_interface_ha1_dict = ha_configurations_interface_ha1_instance.to_dict()
# create an instance of HaConfigurationsInterfaceHa1 from a dict
ha_configurations_interface_ha1_from_dict = HaConfigurationsInterfaceHa1.from_dict(ha_configurations_interface_ha1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


