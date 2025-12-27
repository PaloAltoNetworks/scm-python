# LogForwardingProfilesMatchListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_desc** | **str** | Match profile description | [optional] 
**filter** | **str** | Filter match criteria | [optional] 
**log_type** | **str** | Log type | [optional] 
**name** | **str** | Name of the match profile | [optional] 
**send_http** | **List[str]** | A list of HTTP server profiles | [optional] 
**send_syslog** | **List[str]** | A list of syslog server profiles | [optional] 

## Example

```python
from scm_objects.models.log_forwarding_profiles_match_list_inner import LogForwardingProfilesMatchListInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwardingProfilesMatchListInner from a JSON string
log_forwarding_profiles_match_list_inner_instance = LogForwardingProfilesMatchListInner.from_json(json)
# print the JSON string representation of the object
print(LogForwardingProfilesMatchListInner.to_json())

# convert the object into a dict
log_forwarding_profiles_match_list_inner_dict = log_forwarding_profiles_match_list_inner_instance.to_dict()
# create an instance of LogForwardingProfilesMatchListInner from a dict
log_forwarding_profiles_match_list_inner_from_dict = LogForwardingProfilesMatchListInner.from_dict(log_forwarding_profiles_match_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


