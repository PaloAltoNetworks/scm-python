# SnippetCategoriesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SnippetCategories]**](SnippetCategories.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.config_setup.models.snippet_categories_list_response import SnippetCategoriesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetCategoriesListResponse from a JSON string
snippet_categories_list_response_instance = SnippetCategoriesListResponse.from_json(json)
# print the JSON string representation of the object
print(SnippetCategoriesListResponse.to_json())

# convert the object into a dict
snippet_categories_list_response_dict = snippet_categories_list_response_instance.to_dict()
# create an instance of SnippetCategoriesListResponse from a dict
snippet_categories_list_response_from_dict = SnippetCategoriesListResponse.from_dict(snippet_categories_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


