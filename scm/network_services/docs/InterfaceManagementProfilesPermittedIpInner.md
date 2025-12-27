# InterfaceManagementProfilesPermittedIpInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The allowed IP address or CIDR block. | 

## Example

```python
from scm_network_services.models.interface_management_profiles_permitted_ip_inner import InterfaceManagementProfilesPermittedIpInner

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceManagementProfilesPermittedIpInner from a JSON string
interface_management_profiles_permitted_ip_inner_instance = InterfaceManagementProfilesPermittedIpInner.from_json(json)
# print the JSON string representation of the object
print(InterfaceManagementProfilesPermittedIpInner.to_json())

# convert the object into a dict
interface_management_profiles_permitted_ip_inner_dict = interface_management_profiles_permitted_ip_inner_instance.to_dict()
# create an instance of InterfaceManagementProfilesPermittedIpInner from a dict
interface_management_profiles_permitted_ip_inner_from_dict = InterfaceManagementProfilesPermittedIpInner.from_dict(interface_management_profiles_permitted_ip_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


