# AuthenticationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**AuthenticationSettingsAuthentication**](AuthenticationSettingsAuthentication.md) |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [readonly] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_device_settings.models.authentication_settings import AuthenticationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationSettings from a JSON string
authentication_settings_instance = AuthenticationSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticationSettings.to_json())

# convert the object into a dict
authentication_settings_dict = authentication_settings_instance.to_dict()
# create an instance of AuthenticationSettings from a dict
authentication_settings_from_dict = AuthenticationSettings.from_dict(authentication_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


