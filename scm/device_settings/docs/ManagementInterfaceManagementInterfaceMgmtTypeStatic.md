# ManagementInterfaceManagementInterfaceMgmtTypeStatic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_gateway** | **str** | Default gateway | 
**ip_address** | **str** | IP address | 
**netmask** | **str** | Netmask | 

## Example

```python
from scm_device_settings.models.management_interface_management_interface_mgmt_type_static import ManagementInterfaceManagementInterfaceMgmtTypeStatic

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementInterfaceManagementInterfaceMgmtTypeStatic from a JSON string
management_interface_management_interface_mgmt_type_static_instance = ManagementInterfaceManagementInterfaceMgmtTypeStatic.from_json(json)
# print the JSON string representation of the object
print(ManagementInterfaceManagementInterfaceMgmtTypeStatic.to_json())

# convert the object into a dict
management_interface_management_interface_mgmt_type_static_dict = management_interface_management_interface_mgmt_type_static_instance.to_dict()
# create an instance of ManagementInterfaceManagementInterfaceMgmtTypeStatic from a dict
management_interface_management_interface_mgmt_type_static_from_dict = ManagementInterfaceManagementInterfaceMgmtTypeStatic.from_dict(management_interface_management_interface_mgmt_type_static_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


