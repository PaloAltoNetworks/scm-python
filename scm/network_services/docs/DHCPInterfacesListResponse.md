# DHCPInterfacesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DhcpInterfaces]**](DhcpInterfaces.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_network_services.models.dhcp_interfaces_list_response import DHCPInterfacesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPInterfacesListResponse from a JSON string
dhcp_interfaces_list_response_instance = DHCPInterfacesListResponse.from_json(json)
# print the JSON string representation of the object
print(DHCPInterfacesListResponse.to_json())

# convert the object into a dict
dhcp_interfaces_list_response_dict = dhcp_interfaces_list_response_instance.to_dict()
# create an instance of DHCPInterfacesListResponse from a dict
dhcp_interfaces_list_response_from_dict = DHCPInterfacesListResponse.from_dict(dhcp_interfaces_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


