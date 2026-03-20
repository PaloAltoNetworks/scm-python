# ServiceSettingsServicesNtpServers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_ntp_server** | [**ServiceSettingsServicesNtpServersPrimaryNtpServer**](ServiceSettingsServicesNtpServersPrimaryNtpServer.md) |  | [optional] 
**secondary_ntp_server** | [**ServiceSettingsServicesNtpServersPrimaryNtpServer**](ServiceSettingsServicesNtpServersPrimaryNtpServer.md) |  | [optional] 

## Example

```python
from scm.device_settings.models.service_settings_services_ntp_servers import ServiceSettingsServicesNtpServers

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettingsServicesNtpServers from a JSON string
service_settings_services_ntp_servers_instance = ServiceSettingsServicesNtpServers.from_json(json)
# print the JSON string representation of the object
print(ServiceSettingsServicesNtpServers.to_json())

# convert the object into a dict
service_settings_services_ntp_servers_dict = service_settings_services_ntp_servers_instance.to_dict()
# create an instance of ServiceSettingsServicesNtpServers from a dict
service_settings_services_ntp_servers_from_dict = ServiceSettingsServicesNtpServers.from_dict(service_settings_services_ntp_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


