# ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKeyAlgorithm**](ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKeyAlgorithm.md) |  | [optional] 
**key_id** | **float** |  | [optional] 

## Example

```python
from scm.device_settings.models.service_settings_services_ntp_servers_primary_ntp_server_authentication_type_symmetric_key import ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKey

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKey from a JSON string
service_settings_services_ntp_servers_primary_ntp_server_authentication_type_symmetric_key_instance = ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKey.from_json(json)
# print the JSON string representation of the object
print(ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKey.to_json())

# convert the object into a dict
service_settings_services_ntp_servers_primary_ntp_server_authentication_type_symmetric_key_dict = service_settings_services_ntp_servers_primary_ntp_server_authentication_type_symmetric_key_instance.to_dict()
# create an instance of ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKey from a dict
service_settings_services_ntp_servers_primary_ntp_server_authentication_type_symmetric_key_from_dict = ServiceSettingsServicesNtpServersPrimaryNtpServerAuthenticationTypeSymmetricKey.from_dict(service_settings_services_ntp_servers_primary_ntp_server_authentication_type_symmetric_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


