# ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autokey** | **object** |  | [optional] 
**var_none** | **object** |  | [optional] 
**symmetric_key** | [**ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKey**](ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKey.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.service_settings_services_ntp_servers_primary_ntp_server_authentication_type import ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationType

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationType from a JSON string
service_settings_services_ntp_servers_primary_ntp_server_authentication_type_instance = ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationType.from_json(json)
# print the JSON string representation of the object
print(ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationType.to_json())

# convert the object into a dict
service_settings_services_ntp_servers_primary_ntp_server_authentication_type_dict = service_settings_services_ntp_servers_primary_ntp_server_authentication_type_instance.to_dict()
# create an instance of ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationType from a dict
service_settings_services_ntp_servers_primary_ntp_server_authentication_type_from_dict = ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationType.from_dict(service_settings_services_ntp_servers_primary_ntp_server_authentication_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


