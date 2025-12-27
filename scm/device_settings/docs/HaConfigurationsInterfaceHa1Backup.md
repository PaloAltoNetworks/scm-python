# HaConfigurationsInterfaceHa1Backup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | HA1 backup default gateway | [optional] 
**ip_address** | **str** | HA1 backup IP address | [optional] 
**netmask** | **str** | HA1 backup netmask | [optional] 
**port** | **str** | HA1 backup port | [optional] 

## Example

```python
from scm_device_settings.models.ha_configurations_interface_ha1_backup import HaConfigurationsInterfaceHa1Backup

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsInterfaceHa1Backup from a JSON string
ha_configurations_interface_ha1_backup_instance = HaConfigurationsInterfaceHa1Backup.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsInterfaceHa1Backup.to_json())

# convert the object into a dict
ha_configurations_interface_ha1_backup_dict = ha_configurations_interface_ha1_backup_instance.to_dict()
# create an instance of HaConfigurationsInterfaceHa1Backup from a dict
ha_configurations_interface_ha1_backup_from_dict = HaConfigurationsInterfaceHa1Backup.from_dict(ha_configurations_interface_ha1_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


