# InterfaceManagementProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**http** | **bool** | Allow HTTP? | [optional] 
**http_ocsp** | **bool** | Allow HTTP OCSP? | [optional] 
**https** | **bool** | Allow HTTPS? | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Name | 
**permitted_ip** | [**List[InterfaceManagementProfilesPermittedIpInner]**](InterfaceManagementProfilesPermittedIpInner.md) | Allowed IP address(es) | [optional] 
**ping** | **bool** | Allow ping? | [optional] 
**response_pages** | **bool** | Allow response pages? | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**ssh** | **bool** | Allow SSH? | [optional] 
**telnet** | **bool** | Allow telnet? Seriously, why would you do this?!? | [optional] 
**userid_service** | **bool** | Allow User-ID? | [optional] 
**userid_syslog_listener_ssl** | **bool** | Allow User-ID syslog listener (SSL)? | [optional] 
**userid_syslog_listener_udp** | **bool** | Allow User-ID syslog listener (UDP)? | [optional] 

## Example

```python
from scm_network_services.models.interface_management_profiles import InterfaceManagementProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceManagementProfiles from a JSON string
interface_management_profiles_instance = InterfaceManagementProfiles.from_json(json)
# print the JSON string representation of the object
print(InterfaceManagementProfiles.to_json())

# convert the object into a dict
interface_management_profiles_dict = interface_management_profiles_instance.to_dict()
# create an instance of InterfaceManagementProfiles from a dict
interface_management_profiles_from_dict = InterfaceManagementProfiles.from_dict(interface_management_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


