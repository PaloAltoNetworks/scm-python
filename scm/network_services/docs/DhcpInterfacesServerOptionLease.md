# DhcpInterfacesServerOptionLease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | DHCP lease timeout (minutes) | [optional] 
**unlimited** | **object** |  | [optional] 

## Example

```python
from scm.network_services.models.dhcp_interfaces_server_option_lease import DhcpInterfacesServerOptionLease

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesServerOptionLease from a JSON string
dhcp_interfaces_server_option_lease_instance = DhcpInterfacesServerOptionLease.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesServerOptionLease.to_json())

# convert the object into a dict
dhcp_interfaces_server_option_lease_dict = dhcp_interfaces_server_option_lease_instance.to_dict()
# create an instance of DhcpInterfacesServerOptionLease from a dict
dhcp_interfaces_server_option_lease_from_dict = DhcpInterfacesServerOptionLease.from_dict(dhcp_interfaces_server_option_lease_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


