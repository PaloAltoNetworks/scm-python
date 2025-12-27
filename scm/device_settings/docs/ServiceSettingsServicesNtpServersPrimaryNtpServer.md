# ServiceSettingsServicesNtpServersPrimaryNtpServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | [**ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationType**](ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationType.md) |  | [optional] 
**ntp_server_address** | **str** |  | [optional] 

## Example

```python
from scm_device_settings.models.service_settings_services_ntp_servers_primary_ntp_server import ServiceSettingsServicesNtpServersPrimaryNtpServer

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettingsServicesNtpServersPrimaryNtpServer from a JSON string
service_settings_services_ntp_servers_primary_ntp_server_instance = ServiceSettingsServicesNtpServersPrimaryNtpServer.from_json(json)
# print the JSON string representation of the object
print(ServiceSettingsServicesNtpServersPrimaryNtpServer.to_json())

# convert the object into a dict
service_settings_services_ntp_servers_primary_ntp_server_dict = service_settings_services_ntp_servers_primary_ntp_server_instance.to_dict()
# create an instance of ServiceSettingsServicesNtpServersPrimaryNtpServer from a dict
service_settings_services_ntp_servers_primary_ntp_server_from_dict = ServiceSettingsServicesNtpServersPrimaryNtpServer.from_dict(service_settings_services_ntp_servers_primary_ntp_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


