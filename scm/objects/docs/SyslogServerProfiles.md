# SyslogServerProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**format** | [**SyslogServerProfilesFormat**](SyslogServerProfilesFormat.md) |  | [optional] 
**id** | **str** | The UUID of the syslog server profile | [readonly] 
**name** | **str** | The name of the syslog server profile | 
**server** | [**List[SyslogServerProfilesServerInner]**](SyslogServerProfilesServerInner.md) | A list of syslog server configurations. At least one server is required. | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_objects.models.syslog_server_profiles import SyslogServerProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of SyslogServerProfiles from a JSON string
syslog_server_profiles_instance = SyslogServerProfiles.from_json(json)
# print the JSON string representation of the object
print(SyslogServerProfiles.to_json())

# convert the object into a dict
syslog_server_profiles_dict = syslog_server_profiles_instance.to_dict()
# create an instance of SyslogServerProfiles from a dict
syslog_server_profiles_from_dict = SyslogServerProfiles.from_dict(syslog_server_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


