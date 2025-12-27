# SessionSettingsSessionSettingsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rematch** | **bool** | Rematch all sessions on config policy change | [optional] [default to False]

## Example

```python
from scm.device_settings.models.session_settings_session_settings_config import SessionSettingsSessionSettingsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSettingsSessionSettingsConfig from a JSON string
session_settings_session_settings_config_instance = SessionSettingsSessionSettingsConfig.from_json(json)
# print the JSON string representation of the object
print(SessionSettingsSessionSettingsConfig.to_json())

# convert the object into a dict
session_settings_session_settings_config_dict = session_settings_session_settings_config_instance.to_dict()
# create an instance of SessionSettingsSessionSettingsConfig from a dict
session_settings_session_settings_config_from_dict = SessionSettingsSessionSettingsConfig.from_dict(session_settings_session_settings_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


