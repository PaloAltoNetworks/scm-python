# UrlCategories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**list** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**type** | **str** |  | [optional] [default to 'URL List']

## Example

```python
from scm.security_services.models.url_categories import UrlCategories

# TODO update the JSON string below
json = "{}"
# create an instance of UrlCategories from a JSON string
url_categories_instance = UrlCategories.from_json(json)
# print the JSON string representation of the object
print(UrlCategories.to_json())

# convert the object into a dict
url_categories_dict = url_categories_instance.to_dict()
# create an instance of UrlCategories from a dict
url_categories_from_dict = UrlCategories.from_dict(url_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


