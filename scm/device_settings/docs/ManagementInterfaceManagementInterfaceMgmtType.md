# ManagementInterfaceManagementInterfaceMgmtType

IP type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_client** | [**ManagementInterfaceManagementInterfaceMgmtTypeDhcpClient**](ManagementInterfaceManagementInterfaceMgmtTypeDhcpClient.md) |  | [optional] 
**static** | **object** |  | [optional] 

## Example

```python
from scm.device_settings.models.management_interface_management_interface_mgmt_type import ManagementInterfaceManagementInterfaceMgmtType

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementInterfaceManagementInterfaceMgmtType from a JSON string
management_interface_management_interface_mgmt_type_instance = ManagementInterfaceManagementInterfaceMgmtType.from_json(json)
# print the JSON string representation of the object
print(ManagementInterfaceManagementInterfaceMgmtType.to_json())

# convert the object into a dict
management_interface_management_interface_mgmt_type_dict = management_interface_management_interface_mgmt_type_instance.to_dict()
# create an instance of ManagementInterfaceManagementInterfaceMgmtType from a dict
management_interface_management_interface_mgmt_type_from_dict = ManagementInterfaceManagementInterfaceMgmtType.from_dict(management_interface_management_interface_mgmt_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


