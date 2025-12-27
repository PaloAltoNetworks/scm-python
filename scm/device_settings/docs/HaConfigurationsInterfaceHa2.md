# HaConfigurationsInterfaceHa2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | HA2 default gateway | [optional] 
**ip_address** | **str** | HA2 IP address | 
**netmask** | **str** | HA2 netmask | 
**port** | **str** | HA2 port | 

## Example

```python
from scm_device_settings.models.ha_configurations_interface_ha2 import HaConfigurationsInterfaceHa2

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurationsInterfaceHa2 from a JSON string
ha_configurations_interface_ha2_instance = HaConfigurationsInterfaceHa2.from_json(json)
# print the JSON string representation of the object
print(HaConfigurationsInterfaceHa2.to_json())

# convert the object into a dict
ha_configurations_interface_ha2_dict = ha_configurations_interface_ha2_instance.to_dict()
# create an instance of HaConfigurationsInterfaceHa2 from a dict
ha_configurations_interface_ha2_from_dict = HaConfigurationsInterfaceHa2.from_dict(ha_configurations_interface_ha2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


