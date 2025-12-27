# URLCategoriesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UrlCategories]**](UrlCategories.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_security_services.models.url_categories_list_response import URLCategoriesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of URLCategoriesListResponse from a JSON string
url_categories_list_response_instance = URLCategoriesListResponse.from_json(json)
# print the JSON string representation of the object
print(URLCategoriesListResponse.to_json())

# convert the object into a dict
url_categories_list_response_dict = url_categories_list_response_instance.to_dict()
# create an instance of URLCategoriesListResponse from a dict
url_categories_list_response_from_dict = URLCategoriesListResponse.from_dict(url_categories_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


