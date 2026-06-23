# ConnectorsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Connectors]**](Connectors.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.ztna_connector_all.models.connectors_list_response import ConnectorsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorsListResponse from a JSON string
connectors_list_response_instance = ConnectorsListResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectorsListResponse.to_json())

# convert the object into a dict
connectors_list_response_dict = connectors_list_response_instance.to_dict()
# create an instance of ConnectorsListResponse from a dict
connectors_list_response_from_dict = ConnectorsListResponse.from_dict(connectors_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


