# ServiceSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**services** | [**ServiceSettingsServices**](ServiceSettingsServices.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.device_settings.models.service_settings import ServiceSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettings from a JSON string
service_settings_instance = ServiceSettings.from_json(json)
# print the JSON string representation of the object
print(ServiceSettings.to_json())

# convert the object into a dict
service_settings_dict = service_settings_instance.to_dict()
# create an instance of ServiceSettings from a dict
service_settings_from_dict = ServiceSettings.from_dict(service_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


