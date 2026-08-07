# ForwardingProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition_method** | **str** | Enable forwarding rule for forwarding profile | [optional] [default to 'rules']
**description** | **str** | Forwarding profile description | [optional] 
**id** | **str** | The UUID of the forwarding profile | [optional] [readonly] 
**name** | **str** | forwarding profile name as an alphanumeric string [ 0-9a-zA-Z._ -] | 
**type** | [**ForwardingProfilesType**](ForwardingProfilesType.md) |  | [optional] 

## Example

```python
from scm.mobile_agent.models.forwarding_profiles import ForwardingProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfiles from a JSON string
forwarding_profiles_instance = ForwardingProfiles.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfiles.to_json())

# convert the object into a dict
forwarding_profiles_dict = forwarding_profiles_instance.to_dict()
# create an instance of ForwardingProfiles from a dict
forwarding_profiles_from_dict = ForwardingProfiles.from_dict(forwarding_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


