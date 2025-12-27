# Snippets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the snippet | [optional] 
**id** | **str** | The UUID of the snippet | [readonly] 
**labels** | **List[str]** | Labels applied to the snippet | [optional] 
**name** | **str** | The name of the snippet | 
**type** | **str** | The snippet type | [optional] [readonly] 

## Example

```python
from scm_config_setup.models.snippets import Snippets

# TODO update the JSON string below
json = "{}"
# create an instance of Snippets from a JSON string
snippets_instance = Snippets.from_json(json)
# print the JSON string representation of the object
print(Snippets.to_json())

# convert the object into a dict
snippets_dict = snippets_instance.to_dict()
# create an instance of Snippets from a dict
snippets_from_dict = Snippets.from_dict(snippets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


