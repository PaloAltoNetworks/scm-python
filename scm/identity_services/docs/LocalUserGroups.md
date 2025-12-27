# LocalUserGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the local user group | [readonly] 
**name** | **str** | The name of the local user group | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**user** | **List[str]** | The local user group users | [optional] 

## Example

```python
from scm_identity_services.models.local_user_groups import LocalUserGroups

# TODO update the JSON string below
json = "{}"
# create an instance of LocalUserGroups from a JSON string
local_user_groups_instance = LocalUserGroups.from_json(json)
# print the JSON string representation of the object
print(LocalUserGroups.to_json())

# convert the object into a dict
local_user_groups_dict = local_user_groups_instance.to_dict()
# create an instance of LocalUserGroups from a dict
local_user_groups_from_dict = LocalUserGroups.from_dict(local_user_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


