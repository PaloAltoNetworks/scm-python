# SnippetsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Snippets]**](Snippets.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_config_setup.models.snippets_list_response import SnippetsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetsListResponse from a JSON string
snippets_list_response_instance = SnippetsListResponse.from_json(json)
# print the JSON string representation of the object
print(SnippetsListResponse.to_json())

# convert the object into a dict
snippets_list_response_dict = snippets_list_response_instance.to_dict()
# create an instance of SnippetsListResponse from a dict
snippets_list_response_from_dict = SnippetsListResponse.from_dict(snippets_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


