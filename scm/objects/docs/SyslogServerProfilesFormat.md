# SyslogServerProfilesFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | **str** |  | [optional] 
**config** | **str** |  | [optional] 
**correlation** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**decryption** | **str** |  | [optional] 
**escaping** | [**SyslogServerProfilesFormatEscaping**](SyslogServerProfilesFormatEscaping.md) |  | [optional] 
**globalprotect** | **str** |  | [optional] 
**gtp** | **str** |  | [optional] 
**hip_match** | **str** |  | [optional] 
**iptag** | **str** |  | [optional] 
**sctp** | **str** |  | [optional] 
**system** | **str** |  | [optional] 
**threat** | **str** |  | [optional] 
**traffic** | **str** |  | [optional] 
**tunnel** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**userid** | **str** |  | [optional] 
**wildfire** | **str** |  | [optional] 

## Example

```python
from scm_objects.models.syslog_server_profiles_format import SyslogServerProfilesFormat

# TODO update the JSON string below
json = "{}"
# create an instance of SyslogServerProfilesFormat from a JSON string
syslog_server_profiles_format_instance = SyslogServerProfilesFormat.from_json(json)
# print the JSON string representation of the object
print(SyslogServerProfilesFormat.to_json())

# convert the object into a dict
syslog_server_profiles_format_dict = syslog_server_profiles_format_instance.to_dict()
# create an instance of SyslogServerProfilesFormat from a dict
syslog_server_profiles_format_from_dict = SyslogServerProfilesFormat.from_dict(syslog_server_profiles_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


