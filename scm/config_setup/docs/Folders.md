# Folders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the folder | [optional] 
**id** | **str** | The UUID of the folder | [optional] [readonly] 
**labels** | **List[str]** | Labels assigned to the folder | [optional] 
**name** | **str** | The name of the folder | 
**parent** | **str** | The parent folder | 
**snippets** | **List[str]** | Snippets associated with the folder | [optional] 

## Example

```python
from scm.config_setup.models.folders import Folders

# TODO update the JSON string below
json = "{}"
# create an instance of Folders from a JSON string
folders_instance = Folders.from_json(json)
# print the JSON string representation of the object
print(Folders.to_json())

# convert the object into a dict
folders_dict = folders_instance.to_dict()
# create an instance of Folders from a dict
folders_from_dict = Folders.from_dict(folders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


