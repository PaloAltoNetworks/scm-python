# LocalUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**disabled** | **bool** | Is the local user disabled? | [optional] [default to False]
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the local user | [readonly] 
**name** | **str** | The name of the local user | 
**password** | **str** | The password of the local user | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_identity_services.models.local_users import LocalUsers

# TODO update the JSON string below
json = "{}"
# create an instance of LocalUsers from a JSON string
local_users_instance = LocalUsers.from_json(json)
# print the JSON string representation of the object
print(LocalUsers.to_json())

# convert the object into a dict
local_users_dict = local_users_instance.to_dict()
# create an instance of LocalUsers from a dict
local_users_from_dict = LocalUsers.from_dict(local_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


