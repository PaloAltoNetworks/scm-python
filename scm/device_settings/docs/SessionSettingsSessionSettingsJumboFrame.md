# SessionSettingsSessionSettingsJumboFrame

Enable jumbo frame support

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mtu** | **int** | Global MTU | [optional] [default to 9192]

## Example

```python
from scm_device_settings.models.session_settings_session_settings_jumbo_frame import SessionSettingsSessionSettingsJumboFrame

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSettingsSessionSettingsJumboFrame from a JSON string
session_settings_session_settings_jumbo_frame_instance = SessionSettingsSessionSettingsJumboFrame.from_json(json)
# print the JSON string representation of the object
print(SessionSettingsSessionSettingsJumboFrame.to_json())

# convert the object into a dict
session_settings_session_settings_jumbo_frame_dict = session_settings_session_settings_jumbo_frame_instance.to_dict()
# create an instance of SessionSettingsSessionSettingsJumboFrame from a dict
session_settings_session_settings_jumbo_frame_from_dict = SessionSettingsSessionSettingsJumboFrame.from_dict(session_settings_session_settings_jumbo_frame_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


