# SyslogServerProfilesFormatEscaping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**escape_character** | **str** | Escape sequence delimiter | [optional] 
**escaped_characters** | **str** | A list of all the characters to be escaped (without spaces). | [optional] 

## Example

```python
from scm_objects.models.syslog_server_profiles_format_escaping import SyslogServerProfilesFormatEscaping

# TODO update the JSON string below
json = "{}"
# create an instance of SyslogServerProfilesFormatEscaping from a JSON string
syslog_server_profiles_format_escaping_instance = SyslogServerProfilesFormatEscaping.from_json(json)
# print the JSON string representation of the object
print(SyslogServerProfilesFormatEscaping.to_json())

# convert the object into a dict
syslog_server_profiles_format_escaping_dict = syslog_server_profiles_format_escaping_instance.to_dict()
# create an instance of SyslogServerProfilesFormatEscaping from a dict
syslog_server_profiles_format_escaping_from_dict = SyslogServerProfilesFormatEscaping.from_dict(syslog_server_profiles_format_escaping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


