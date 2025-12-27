# ManagementInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**management_interface** | [**ManagementInterfaceManagementInterface**](ManagementInterfaceManagementInterface.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_device_settings.models.management_interface import ManagementInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementInterface from a JSON string
management_interface_instance = ManagementInterface.from_json(json)
# print the JSON string representation of the object
print(ManagementInterface.to_json())

# convert the object into a dict
management_interface_dict = management_interface_instance.to_dict()
# create an instance of ManagementInterface from a dict
management_interface_from_dict = ManagementInterface.from_dict(management_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


