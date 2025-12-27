# HaConfigurationsInterfaceHa2Backup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | HA2 backup default gateway | [optional] 
**ip_address** | **str** | HA2 backup IP address | [optional] 
**netmask** | **str** | HA2 backup netmask | [optional] 
**port** | **str** | HA2 backup port | [optional] 

## Example

```python
from scm.device_settings.models.ha_configurations_interface_ha2_backup import HaConfigurationsInterfaceHa2Backup

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsInterfaceHa2Backup from a JSON string
ha_configurations_interface_ha2_backup_instance = HaConfigurationsInterfaceHa2Backup.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsInterfaceHa2Backup.to_json())

# convert the object into a dict
ha_configurations_interface_ha2_backup_dict = ha_configurations_interface_ha2_backup_instance.to_dict()
# create an instance of HaConfigurationsInterfaceHa2Backup from a dict
ha_configurations_interface_ha2_backup_from_dict = HaConfigurationsInterfaceHa2Backup.from_dict(ha_configurations_interface_ha2_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


