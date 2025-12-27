# DhcpInterfacesServerOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | [**DhcpInterfacesServerOptionDns**](DhcpInterfacesServerOptionDns.md) |  | [optional] 
**dns_suffix** | **str** | DNS suffix | [optional] 
**gateway** | **str** | Default gateway | [optional] 
**inheritance** | [**DhcpInterfacesServerOptionInheritance**](DhcpInterfacesServerOptionInheritance.md) |  | [optional] 
**lease** | [**DhcpInterfacesServerOptionLease**](DhcpInterfacesServerOptionLease.md) |  | [optional] 
**nis** | [**DhcpInterfacesServerOptionNis**](DhcpInterfacesServerOptionNis.md) |  | [optional] 
**ntp** | [**DhcpInterfacesServerOptionNtp**](DhcpInterfacesServerOptionNtp.md) |  | [optional] 
**pop3_server** | **str** | POP3 server | [optional] 
**smtp_server** | **str** | SMTP server | [optional] 
**subnet_mask** | **str** | Subnet mask | [optional] 
**user_defined** | [**List[DhcpInterfacesServerOptionUserDefinedInner]**](DhcpInterfacesServerOptionUserDefinedInner.md) | Custom DHCP options | [optional] 
**wins** | [**DhcpInterfacesServerOptionWins**](DhcpInterfacesServerOptionWins.md) |  | [optional] 

## Example

```python
from scm.network_services.models.dhcp_interfaces_server_option import DhcpInterfacesServerOption

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesServerOption from a JSON string
dhcp_interfaces_server_option_instance = DhcpInterfacesServerOption.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesServerOption.to_json())

# convert the object into a dict
dhcp_interfaces_server_option_dict = dhcp_interfaces_server_option_instance.to_dict()
# create an instance of DhcpInterfacesServerOption from a dict
dhcp_interfaces_server_option_from_dict = DhcpInterfacesServerOption.from_dict(dhcp_interfaces_server_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


