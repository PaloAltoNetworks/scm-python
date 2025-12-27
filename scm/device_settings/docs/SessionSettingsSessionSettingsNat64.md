# SessionSettingsSessionSettingsNat64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv6_min_network_mtu** | **int** | NAT64 IPv6 minimum network MTU | [optional] [default to 1280]

## Example

```python
from scm_device_settings.models.session_settings_session_settings_nat64 import SessionSettingsSessionSettingsNat64

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSettingsSessionSettingsNat64 from a JSON string
session_settings_session_settings_nat64_instance = SessionSettingsSessionSettingsNat64.from_json(json)
# print the JSON string representation of the object
print(SessionSettingsSessionSettingsNat64.to_json())

# convert the object into a dict
session_settings_session_settings_nat64_dict = session_settings_session_settings_nat64_instance.to_dict()
# create an instance of SessionSettingsSessionSettingsNat64 from a dict
session_settings_session_settings_nat64_from_dict = SessionSettingsSessionSettingsNat64.from_dict(session_settings_session_settings_nat64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


