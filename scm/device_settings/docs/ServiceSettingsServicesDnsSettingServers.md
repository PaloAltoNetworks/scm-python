# ServiceSettingsServicesDnsSettingServers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** |  | [optional] 
**secondary** | **str** |  | [optional] 

## Example

```python
from scm_device_settings.models.service_settings_services_dns_setting_servers import ServiceSettingsServicesDnsSettingServers

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettingsServicesDnsSettingServers from a JSON string
service_settings_services_dns_setting_servers_instance = ServiceSettingsServicesDnsSettingServers.from_json(json)
# print the JSON string representation of the object
print(ServiceSettingsServicesDnsSettingServers.to_json())

# convert the object into a dict
service_settings_services_dns_setting_servers_dict = service_settings_services_dns_setting_servers_instance.to_dict()
# create an instance of ServiceSettingsServicesDnsSettingServers from a dict
service_settings_services_dns_setting_servers_from_dict = ServiceSettingsServicesDnsSettingServers.from_dict(service_settings_services_dns_setting_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


