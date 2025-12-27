# SessionSettingsSessionSettingsIcmpv6RateLimit

ICMPv6 rate limiting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_size** | **int** | ICMPv6 token bucket size | [optional] [default to 100]
**packet_rate** | **int** | ICMPv6 error packet pate (per second) | [optional] [default to 100]

## Example

```python
from scm_device_settings.models.session_settings_session_settings_icmpv6_rate_limit import SessionSettingsSessionSettingsIcmpv6RateLimit

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSettingsSessionSettingsIcmpv6RateLimit from a JSON string
session_settings_session_settings_icmpv6_rate_limit_instance = SessionSettingsSessionSettingsIcmpv6RateLimit.from_json(json)
# print the JSON string representation of the object
print(SessionSettingsSessionSettingsIcmpv6RateLimit.to_json())

# convert the object into a dict
session_settings_session_settings_icmpv6_rate_limit_dict = session_settings_session_settings_icmpv6_rate_limit_instance.to_dict()
# create an instance of SessionSettingsSessionSettingsIcmpv6RateLimit from a dict
session_settings_session_settings_icmpv6_rate_limit_from_dict = SessionSettingsSessionSettingsIcmpv6RateLimit.from_dict(session_settings_session_settings_icmpv6_rate_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


