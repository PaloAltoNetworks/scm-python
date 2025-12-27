# LinkTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The color of the link tag | [optional] 
**comments** | **str** | Description of the link tag | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the link tag | [optional] [readonly] 
**name** | **str** | The name of the link tag | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.network_services.models.link_tags import LinkTags

# TODO update the JSON string below
json = "{}"
# create an instance of LinkTags from a JSON string
link_tags_instance = LinkTags.from_json(json)
# print the JSON string representation of the object
print(LinkTags.to_json())

# convert the object into a dict
link_tags_dict = link_tags_instance.to_dict()
# create an instance of LinkTags from a dict
link_tags_from_dict = LinkTags.from_dict(link_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


