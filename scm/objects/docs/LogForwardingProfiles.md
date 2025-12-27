# LogForwardingProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Log forwarding profile description | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the log server profile | [readonly] 
**match_list** | [**List[LogForwardingProfilesMatchListInner]**](LogForwardingProfilesMatchListInner.md) |  | [optional] 
**name** | **str** | The name of the log forwarding profile | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.objects.models.log_forwarding_profiles import LogForwardingProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwardingProfiles from a JSON string
log_forwarding_profiles_instance = LogForwardingProfiles.from_json(json)
# print the JSON string representation of the object
print(LogForwardingProfiles.to_json())

# convert the object into a dict
log_forwarding_profiles_dict = log_forwarding_profiles_instance.to_dict()
# create an instance of LogForwardingProfiles from a dict
log_forwarding_profiles_from_dict = LogForwardingProfiles.from_dict(log_forwarding_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


