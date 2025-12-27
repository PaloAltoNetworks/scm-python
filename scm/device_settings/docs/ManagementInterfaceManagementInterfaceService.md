# ManagementInterfaceManagementInterfaceService

Network services

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_http** | **bool** | HTTP | [optional] [default to False]
**disable_http_ocsp** | **bool** | HTTP OCSP | [optional] [default to False]
**disable_https** | **bool** | HTTPS | [optional] [default to True]
**disable_icmp** | **bool** | Ping | [optional] [default to False]
**disable_snmp** | **bool** | SNMP | [optional] [default to False]
**disable_ssh** | **bool** | SSH | [optional] [default to True]
**disable_telnet** | **bool** | Telnet | [optional] [default to False]
**disable_userid_service** | **bool** | User-ID | [optional] [default to False]
**disable_userid_syslog_listener_ssl** | **bool** | User-ID syslog listener over SSL | [optional] [default to False]
**disable_userid_syslog_listener_udp** | **bool** | User-ID syslog listener over UDP | [optional] [default to False]

## Example

```python
from scm_device_settings.models.management_interface_management_interface_service import ManagementInterfaceManagementInterfaceService

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementInterfaceManagementInterfaceService from a JSON string
management_interface_management_interface_service_instance = ManagementInterfaceManagementInterfaceService.from_json(json)
# print the JSON string representation of the object
print(ManagementInterfaceManagementInterfaceService.to_json())

# convert the object into a dict
management_interface_management_interface_service_dict = management_interface_management_interface_service_instance.to_dict()
# create an instance of ManagementInterfaceManagementInterfaceService from a dict
management_interface_management_interface_service_from_dict = ManagementInterfaceManagementInterfaceService.from_dict(management_interface_management_interface_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


