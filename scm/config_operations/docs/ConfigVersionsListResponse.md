# ConfigVersionsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConfigVersion]**](ConfigVersion.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.config_operations.models.config_versions_list_response import ConfigVersionsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigVersionsListResponse from a JSON string
config_versions_list_response_instance = ConfigVersionsListResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigVersionsListResponse.to_json())

# convert the object into a dict
config_versions_list_response_dict = config_versions_list_response_instance.to_dict()
# create an instance of ConfigVersionsListResponse from a dict
config_versions_list_response_from_dict = ConfigVersionsListResponse.from_dict(config_versions_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


