# ExternalDynamicListsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExternalDynamicLists]**](ExternalDynamicLists.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_objects.models.external_dynamic_lists_list_response import ExternalDynamicListsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsListResponse from a JSON string
external_dynamic_lists_list_response_instance = ExternalDynamicListsListResponse.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsListResponse.to_json())

# convert the object into a dict
external_dynamic_lists_list_response_dict = external_dynamic_lists_list_response_instance.to_dict()
# create an instance of ExternalDynamicListsListResponse from a dict
external_dynamic_lists_list_response_from_dict = ExternalDynamicListsListResponse.from_dict(external_dynamic_lists_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


