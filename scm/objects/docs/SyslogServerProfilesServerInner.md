# SyslogServerProfilesServerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility** | **str** | Syslog facility | [optional] 
**format** | **str** | Syslog format | [optional] 
**name** | **str** | Syslog server name | [optional] 
**port** | **int** | Syslog server port | [optional] 
**server** | **str** | Syslog server address | [optional] 
**transport** | **str** | Transport protocol | [optional] 

## Example

```python
from scm_objects.models.syslog_server_profiles_server_inner import SyslogServerProfilesServerInner

# TODO update the JSON string below
json = "{}"
# create an instance of SyslogServerProfilesServerInner from a JSON string
syslog_server_profiles_server_inner_instance = SyslogServerProfilesServerInner.from_json(json)
# print the JSON string representation of the object
print(SyslogServerProfilesServerInner.to_json())

# convert the object into a dict
syslog_server_profiles_server_inner_dict = syslog_server_profiles_server_inner_instance.to_dict()
# create an instance of SyslogServerProfilesServerInner from a dict
syslog_server_profiles_server_inner_from_dict = SyslogServerProfilesServerInner.from_dict(syslog_server_profiles_server_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


