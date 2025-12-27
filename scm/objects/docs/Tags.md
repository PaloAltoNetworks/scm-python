# Tags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The color of the tag | [optional] 
**comments** | **str** | The description of the tag | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the tag | [optional] [readonly] 
**name** | **str** | The name of the tag | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_objects.models.tags import Tags

# TODO update the JSON string below
json = "{}"
# create an instance of Tags from a JSON string
tags_instance = Tags.from_json(json)
# print the JSON string representation of the object
print(Tags.to_json())

# convert the object into a dict
tags_dict = tags_instance.to_dict()
# create an instance of Tags from a dict
tags_from_dict = Tags.from_dict(tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


