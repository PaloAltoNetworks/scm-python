# ProfileGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_security** | **List[str]** |  | [optional] 
**data_filtering** | **List[str]** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**dns_security** | **List[str]** |  | [optional] 
**file_blocking** | **List[str]** |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the profile group | [optional] [readonly] 
**name** | **str** | The name of the profile group | 
**saas_security** | **List[str]** |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**spyware** | **List[str]** |  | [optional] 
**url_filtering** | **List[str]** |  | [optional] 
**virus_and_wildfire_analysis** | **List[str]** |  | [optional] 
**vulnerability** | **List[str]** |  | [optional] 

## Example

```python
from scm_security_services.models.profile_groups import ProfileGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileGroups from a JSON string
profile_groups_instance = ProfileGroups.from_json(json)
# print the JSON string representation of the object
print(ProfileGroups.to_json())

# convert the object into a dict
profile_groups_dict = profile_groups_instance.to_dict()
# create an instance of ProfileGroups from a dict
profile_groups_from_dict = ProfileGroups.from_dict(profile_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


