# SessionSettingsSessionSettingsNat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dipp_oversub** | **str** | NAT oversubscription rate | [optional] [default to '1x']

## Example

```python
from scm_device_settings.models.session_settings_session_settings_nat import SessionSettingsSessionSettingsNat

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSettingsSessionSettingsNat from a JSON string
session_settings_session_settings_nat_instance = SessionSettingsSessionSettingsNat.from_json(json)
# print the JSON string representation of the object
print(SessionSettingsSessionSettingsNat.to_json())

# convert the object into a dict
session_settings_session_settings_nat_dict = session_settings_session_settings_nat_instance.to_dict()
# create an instance of SessionSettingsSessionSettingsNat from a dict
session_settings_session_settings_nat_from_dict = SessionSettingsSessionSettingsNat.from_dict(session_settings_session_settings_nat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


