# TunnelInterfacesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TunnelInterfaces]**](TunnelInterfaces.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.tunnel_interfaces_list_response import TunnelInterfacesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelInterfacesListResponse from a JSON string
tunnel_interfaces_list_response_instance = TunnelInterfacesListResponse.from_json(json)
# print the JSON string representation of the object
print(TunnelInterfacesListResponse.to_json())

# convert the object into a dict
tunnel_interfaces_list_response_dict = tunnel_interfaces_list_response_instance.to_dict()
# create an instance of TunnelInterfacesListResponse from a dict
tunnel_interfaces_list_response_from_dict = TunnelInterfacesListResponse.from_dict(tunnel_interfaces_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


