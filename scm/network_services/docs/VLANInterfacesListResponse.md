# VLANInterfacesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VlanInterfaces]**](VlanInterfaces.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.vlan_interfaces_list_response import VLANInterfacesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VLANInterfacesListResponse from a JSON string
vlan_interfaces_list_response_instance = VLANInterfacesListResponse.from_json(json)
# print the JSON string representation of the object
print(VLANInterfacesListResponse.to_json())

# convert the object into a dict
vlan_interfaces_list_response_dict = vlan_interfaces_list_response_instance.to_dict()
# create an instance of VLANInterfacesListResponse from a dict
vlan_interfaces_list_response_from_dict = VLANInterfacesListResponse.from_dict(vlan_interfaces_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


