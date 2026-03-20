# ConfigMatchListListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConfigMatchList]**](ConfigMatchList.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.config_match_list_list_response import ConfigMatchListListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigMatchListListResponse from a JSON string
config_match_list_list_response_instance = ConfigMatchListListResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigMatchListListResponse.to_json())

# convert the object into a dict
config_match_list_list_response_dict = config_match_list_list_response_instance.to_dict()
# create an instance of ConfigMatchListListResponse from a dict
config_match_list_list_response_from_dict = ConfigMatchListListResponse.from_dict(config_match_list_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


