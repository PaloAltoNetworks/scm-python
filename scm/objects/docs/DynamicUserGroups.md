# DynamicUserGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the dynamic address group | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**filter** | **str** | The tag-based filter for the dynamic user group | 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the dynamic user group | [readonly] 
**name** | **str** | The name of the dynamic address group | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**tag** | **List[str]** | Tags associated with the dynamic user group | [optional] 

## Example

```python
from scm.objects.models.dynamic_user_groups import DynamicUserGroups

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicUserGroups from a JSON string
dynamic_user_groups_instance = DynamicUserGroups.from_json(json)
# print the JSON string representation of the object
print(DynamicUserGroups.to_json())

# convert the object into a dict
dynamic_user_groups_dict = dynamic_user_groups_instance.to_dict()
# create an instance of DynamicUserGroups from a dict
dynamic_user_groups_from_dict = DynamicUserGroups.from_dict(dynamic_user_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


