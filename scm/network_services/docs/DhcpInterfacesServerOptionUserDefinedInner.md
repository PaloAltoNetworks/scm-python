# DhcpInterfacesServerOptionUserDefinedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ascii** | **List[str]** |  | [optional] 
**code** | **int** | Option code | [optional] 
**hex** | **List[str]** |  | [optional] 
**inherited** | **bool** | Inherited from DHCP server inheritance source? | 
**ip** | **List[str]** |  | [optional] 
**name** | **str** | Option name | 

## Example

```python
from scm_network_services.models.dhcp_interfaces_server_option_user_defined_inner import DhcpInterfacesServerOptionUserDefinedInner

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesServerOptionUserDefinedInner from a JSON string
dhcp_interfaces_server_option_user_defined_inner_instance = DhcpInterfacesServerOptionUserDefinedInner.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesServerOptionUserDefinedInner.to_json())

# convert the object into a dict
dhcp_interfaces_server_option_user_defined_inner_dict = dhcp_interfaces_server_option_user_defined_inner_instance.to_dict()
# create an instance of DhcpInterfacesServerOptionUserDefinedInner from a dict
dhcp_interfaces_server_option_user_defined_inner_from_dict = DhcpInterfacesServerOptionUserDefinedInner.from_dict(dhcp_interfaces_server_option_user_defined_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


