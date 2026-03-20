# ManagementInterfaceManagementInterfaceMgmtTypeDhcpClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_dhcp_domain** | **bool** | Accept DHCP server provided domain name | [optional] [default to False]
**accept_dhcp_hostname** | **bool** | Accept DHCP server provided hostname | [optional] [default to False]
**send_client_id** | **bool** | Send client ID | [optional] [default to False]
**send_hostname** | **bool** | Send hostname | [optional] [default to False]

## Example

```python
from scm.device_settings.models.management_interface_management_interface_mgmt_type_dhcp_client import ManagementInterfaceManagementInterfaceMgmtTypeDhcpClient

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementInterfaceManagementInterfaceMgmtTypeDhcpClient from a JSON string
management_interface_management_interface_mgmt_type_dhcp_client_instance = ManagementInterfaceManagementInterfaceMgmtTypeDhcpClient.from_json(json)
# print the JSON string representation of the object
print(ManagementInterfaceManagementInterfaceMgmtTypeDhcpClient.to_json())

# convert the object into a dict
management_interface_management_interface_mgmt_type_dhcp_client_dict = management_interface_management_interface_mgmt_type_dhcp_client_instance.to_dict()
# create an instance of ManagementInterfaceManagementInterfaceMgmtTypeDhcpClient from a dict
management_interface_management_interface_mgmt_type_dhcp_client_from_dict = ManagementInterfaceManagementInterfaceMgmtTypeDhcpClient.from_dict(management_interface_management_interface_mgmt_type_dhcp_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


