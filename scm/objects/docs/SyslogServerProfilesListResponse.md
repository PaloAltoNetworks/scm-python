# SyslogServerProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SyslogServerProfiles]**](SyslogServerProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.objects.models.syslog_server_profiles_list_response import SyslogServerProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyslogServerProfilesListResponse from a JSON string
syslog_server_profiles_list_response_instance = SyslogServerProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(SyslogServerProfilesListResponse.to_json())

# convert the object into a dict
syslog_server_profiles_list_response_dict = syslog_server_profiles_list_response_instance.to_dict()
# create an instance of SyslogServerProfilesListResponse from a dict
syslog_server_profiles_list_response_from_dict = SyslogServerProfilesListResponse.from_dict(syslog_server_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


