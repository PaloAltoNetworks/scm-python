# AutoTagActionsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AutoTagActions]**](AutoTagActions.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_objects.models.auto_tag_actions_list_response import AutoTagActionsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTagActionsListResponse from a JSON string
auto_tag_actions_list_response_instance = AutoTagActionsListResponse.from_json(json)
# print the JSON string representation of the object
print(AutoTagActionsListResponse.to_json())

# convert the object into a dict
auto_tag_actions_list_response_dict = auto_tag_actions_list_response_instance.to_dict()
# create an instance of AutoTagActionsListResponse from a dict
auto_tag_actions_list_response_from_dict = AutoTagActionsListResponse.from_dict(auto_tag_actions_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


