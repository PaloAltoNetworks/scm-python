# UsedFolders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from scm.config_setup.models.used_folders import UsedFolders

# TODO update the JSON string below
json = "{}"
# create an instance of UsedFolders from a JSON string
used_folders_instance = UsedFolders.from_json(json)
# print the JSON string representation of the object
print(UsedFolders.to_json())

# convert the object into a dict
used_folders_dict = used_folders_instance.to_dict()
# create an instance of UsedFolders from a dict
used_folders_from_dict = UsedFolders.from_dict(used_folders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


