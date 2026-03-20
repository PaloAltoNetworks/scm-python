# IptagMatchListListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IptagMatchList]**](IptagMatchList.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.iptag_match_list_list_response import IptagMatchListListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IptagMatchListListResponse from a JSON string
iptag_match_list_list_response_instance = IptagMatchListListResponse.from_json(json)
# print the JSON string representation of the object
print(IptagMatchListListResponse.to_json())

# convert the object into a dict
iptag_match_list_list_response_dict = iptag_match_list_list_response_instance.to_dict()
# create an instance of IptagMatchListListResponse from a dict
iptag_match_list_list_response_from_dict = IptagMatchListListResponse.from_dict(iptag_match_list_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


