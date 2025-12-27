# ServiceSettingsServices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_setting** | [**ServiceSettingsServicesDnsSetting**](ServiceSettingsServicesDnsSetting.md) |  | [optional] 
**fqdn_refresh_time** | **float** |  | [optional] [default to 15]
**fqdn_stale_entry_timeout** | **float** |  | [optional] [default to 1440]
**inline_cloud_proxy** | **bool** |  | [optional] [default to False]
**lcaas_use_proxy** | **bool** |  | [optional] [default to False]
**ntp_servers** | [**ServiceSettingsServicesNtpServers**](ServiceSettingsServicesNtpServers.md) |  | [optional] 
**secure_proxy_password** | **str** |  | [optional] 
**secure_proxy_port** | **float** |  | [optional] 
**secure_proxy_server** | **str** |  | [optional] 
**secure_proxy_user** | **str** |  | [optional] 
**server_verification** | **bool** |  | [optional] [default to True]
**update_server** | **str** |  | [optional] [default to 'updates.paloaltonetworks.com']

## Example

```python
from scm.device_settings.models.service_settings_services import ServiceSettingsServices

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettingsServices from a JSON string
service_settings_services_instance = ServiceSettingsServices.from_json(json)
# print the JSON string representation of the object
print(ServiceSettingsServices.to_json())

# convert the object into a dict
service_settings_services_dict = service_settings_services_instance.to_dict()
# create an instance of ServiceSettingsServices from a dict
service_settings_services_from_dict = ServiceSettingsServices.from_dict(service_settings_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


