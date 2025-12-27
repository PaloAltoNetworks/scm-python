# DhcpInterfacesServerOptionDns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | Primary DNS server | [optional] 
**secondary** | **str** | Secondary DNS server | [optional] 

## Example

```python
from scm_network_services.models.dhcp_interfaces_server_option_dns import DhcpInterfacesServerOptionDns

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesServerOptionDns from a JSON string
dhcp_interfaces_server_option_dns_instance = DhcpInterfacesServerOptionDns.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesServerOptionDns.to_json())

# convert the object into a dict
dhcp_interfaces_server_option_dns_dict = dhcp_interfaces_server_option_dns_instance.to_dict()
# create an instance of DhcpInterfacesServerOptionDns from a dict
dhcp_interfaces_server_option_dns_from_dict = DhcpInterfacesServerOptionDns.from_dict(dhcp_interfaces_server_option_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


