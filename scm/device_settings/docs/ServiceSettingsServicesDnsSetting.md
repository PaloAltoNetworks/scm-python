# ServiceSettingsServicesDnsSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_proxy_object** | **str** |  | [optional] 
**servers** | [**ServiceSettingsServicesDnsSettingServers**](ServiceSettingsServicesDnsSettingServers.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.service_settings_services_dns_setting import ServiceSettingsServicesDnsSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettingsServicesDnsSetting from a JSON string
service_settings_services_dns_setting_instance = ServiceSettingsServicesDnsSetting.from_json(json)
# print the JSON string representation of the object
print(ServiceSettingsServicesDnsSetting.to_json())

# convert the object into a dict
service_settings_services_dns_setting_dict = service_settings_services_dns_setting_instance.to_dict()
# create an instance of ServiceSettingsServicesDnsSetting from a dict
service_settings_services_dns_setting_from_dict = ServiceSettingsServicesDnsSetting.from_dict(service_settings_services_dns_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


