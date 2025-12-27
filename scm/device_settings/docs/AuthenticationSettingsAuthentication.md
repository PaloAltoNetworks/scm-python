# AuthenticationSettingsAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_server_profile** | **str** | Accounting server profile | [optional] 
**authentication_profile** | **str** | Authentication profile | [optional] 
**certificate_profile** | **str** | Certificate profile | [optional] 

## Example

```python
from scm_device_settings.models.authentication_settings_authentication import AuthenticationSettingsAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationSettingsAuthentication from a JSON string
authentication_settings_authentication_instance = AuthenticationSettingsAuthentication.from_json(json)
# print the JSON string representation of the object
print(AuthenticationSettingsAuthentication.to_json())

# convert the object into a dict
authentication_settings_authentication_dict = authentication_settings_authentication_instance.to_dict()
# create an instance of AuthenticationSettingsAuthentication from a dict
authentication_settings_authentication_from_dict = AuthenticationSettingsAuthentication.from_dict(authentication_settings_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


