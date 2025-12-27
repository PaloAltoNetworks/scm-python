# LoopbackInterfacesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LoopbackInterfaces]**](LoopbackInterfaces.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.loopback_interfaces_list_response import LoopbackInterfacesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoopbackInterfacesListResponse from a JSON string
loopback_interfaces_list_response_instance = LoopbackInterfacesListResponse.from_json(json)
# print the JSON string representation of the object
print(LoopbackInterfacesListResponse.to_json())

# convert the object into a dict
loopback_interfaces_list_response_dict = loopback_interfaces_list_response_instance.to_dict()
# create an instance of LoopbackInterfacesListResponse from a dict
loopback_interfaces_list_response_from_dict = LoopbackInterfacesListResponse.from_dict(loopback_interfaces_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


