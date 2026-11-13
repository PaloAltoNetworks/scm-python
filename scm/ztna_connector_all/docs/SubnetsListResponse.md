# SubnetsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Subnets]**](Subnets.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.ztna_connector_all.models.subnets_list_response import SubnetsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetsListResponse from a JSON string
subnets_list_response_instance = SubnetsListResponse.from_json(json)
# print the JSON string representation of the object
print(SubnetsListResponse.to_json())

# convert the object into a dict
subnets_list_response_dict = subnets_list_response_instance.to_dict()
# create an instance of SubnetsListResponse from a dict
subnets_list_response_from_dict = SubnetsListResponse.from_dict(subnets_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


