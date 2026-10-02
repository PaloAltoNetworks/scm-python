# ForwardingProfileSourceApplications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | **List[str]** | List of application names to be included in this source application profile | 
**description** | **str** | fowarding profile source application description | [optional] 
**id** | **str** | The id of the source application | [optional] [readonly] 
**name** | **str** | The unique name identifying the source application. Must be alphanumeric with allowed characters [0-9a-zA-Z._-] | 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_source_applications import ForwardingProfileSourceApplications

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileSourceApplications from a JSON string
forwarding_profile_source_applications_instance = ForwardingProfileSourceApplications.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileSourceApplications.to_json())

# convert the object into a dict
forwarding_profile_source_applications_dict = forwarding_profile_source_applications_instance.to_dict()
# create an instance of ForwardingProfileSourceApplications from a dict
forwarding_profile_source_applications_from_dict = ForwardingProfileSourceApplications.from_dict(forwarding_profile_source_applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


