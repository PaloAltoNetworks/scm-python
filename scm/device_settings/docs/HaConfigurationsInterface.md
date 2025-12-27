# HaConfigurationsInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ha1** | [**HaConfigurationsInterfaceHa1**](HaConfigurationsInterfaceHa1.md) |  | 
**ha1_backup** | [**HaConfigurationsInterfaceHa1Backup**](HaConfigurationsInterfaceHa1Backup.md) |  | [optional] 
**ha2** | [**HaConfigurationsInterfaceHa2**](HaConfigurationsInterfaceHa2.md) |  | 
**ha2_backup** | [**HaConfigurationsInterfaceHa2Backup**](HaConfigurationsInterfaceHa2Backup.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.ha_configurations_interface import HaConfigurationsInterface

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsInterface from a JSON string
ha_configurations_interface_instance = HaConfigurationsInterface.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsInterface.to_json())

# convert the object into a dict
ha_configurations_interface_dict = ha_configurations_interface_instance.to_dict()
# create an instance of HaConfigurationsInterface from a dict
ha_configurations_interface_from_dict = HaConfigurationsInterface.from_dict(ha_configurations_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


