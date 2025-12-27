# UrlFilteringCategories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from scm_security_services.models.url_filtering_categories import UrlFilteringCategories

# TODO update the JSON string below
json = "{}"
# create an instance of UrlFilteringCategories from a JSON string
url_filtering_categories_instance = UrlFilteringCategories.from_json(json)
# print the JSON string representation of the object
print(UrlFilteringCategories.to_json())

# convert the object into a dict
url_filtering_categories_dict = url_filtering_categories_instance.to_dict()
# create an instance of UrlFilteringCategories from a dict
url_filtering_categories_from_dict = UrlFilteringCategories.from_dict(url_filtering_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


