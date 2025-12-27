# ManagementInterfaceManagementInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mgmt_type** | [**ManagementInterfaceManagementInterfaceMgmtType**](ManagementInterfaceManagementInterfaceMgmtType.md) |  | [optional] 
**mtu** | **int** | MTU | [optional] [default to 1500]
**permitted_ip** | [**List[ManagementInterfaceManagementInterfacePermittedIpInner]**](ManagementInterfaceManagementInterfacePermittedIpInner.md) | Permitting IP addresses | [optional] 
**service** | [**ManagementInterfaceManagementInterfaceService**](ManagementInterfaceManagementInterfaceService.md) |  | [optional] 
**speed_duplex** | **str** | Speed and duplex | [optional] [default to 'auto-negotiate']

## Example

```python
from scm.device_settings.models.management_interface_management_interface import ManagementInterfaceManagementInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementInterfaceManagementInterface from a JSON string
management_interface_management_interface_instance = ManagementInterfaceManagementInterface.from_json(json)
# print the JSON string representation of the object
print(ManagementInterfaceManagementInterface.to_json())

# convert the object into a dict
management_interface_management_interface_dict = management_interface_management_interface_instance.to_dict()
# create an instance of ManagementInterfaceManagementInterface from a dict
management_interface_management_interface_from_dict = ManagementInterfaceManagementInterface.from_dict(management_interface_management_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


