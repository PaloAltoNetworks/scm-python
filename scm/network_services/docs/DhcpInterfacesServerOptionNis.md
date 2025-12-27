# DhcpInterfacesServerOptionNis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | Primary NIS server | [optional] 
**secondary** | **str** | Secondary NIS server | [optional] 

## Example

```python
from scm_network_services.models.dhcp_interfaces_server_option_nis import DhcpInterfacesServerOptionNis

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesServerOptionNis from a JSON string
dhcp_interfaces_server_option_nis_instance = DhcpInterfacesServerOptionNis.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesServerOptionNis.to_json())

# convert the object into a dict
dhcp_interfaces_server_option_nis_dict = dhcp_interfaces_server_option_nis_instance.to_dict()
# create an instance of DhcpInterfacesServerOptionNis from a dict
dhcp_interfaces_server_option_nis_from_dict = DhcpInterfacesServerOptionNis.from_dict(dhcp_interfaces_server_option_nis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


