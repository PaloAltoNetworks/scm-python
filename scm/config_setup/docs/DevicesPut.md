# DevicesPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the device | [optional] 
**display_name** | **str** | The display name of the device | [optional] 
**folder** | **str** | The folder containing the device | [optional] 
**labels** | **List[str]** | Labels assigned to the device | [optional] 
**snippets** | **List[str]** | Snippets associated with the device | [optional] 

## Example

```python
from scm_config_setup.models.devices_put import DevicesPut

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesPut from a JSON string
devices_put_instance = DevicesPut.from_json(json)
# print the JSON string representation of the object
print(DevicesPut.to_json())

# convert the object into a dict
devices_put_dict = devices_put_instance.to_dict()
# create an instance of DevicesPut from a dict
devices_put_from_dict = DevicesPut.from_dict(devices_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


