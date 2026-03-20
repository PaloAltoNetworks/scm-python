# DhcpInterfacesServerOptionNtp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | Primary NTP server | [optional] 
**secondary** | **str** | Secondary NTP server | [optional] 

## Example

```python
from scm.network_services.models.dhcp_interfaces_server_option_ntp import DhcpInterfacesServerOptionNtp

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesServerOptionNtp from a JSON string
dhcp_interfaces_server_option_ntp_instance = DhcpInterfacesServerOptionNtp.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesServerOptionNtp.to_json())

# convert the object into a dict
dhcp_interfaces_server_option_ntp_dict = dhcp_interfaces_server_option_ntp_instance.to_dict()
# create an instance of DhcpInterfacesServerOptionNtp from a dict
dhcp_interfaces_server_option_ntp_from_dict = DhcpInterfacesServerOptionNtp.from_dict(dhcp_interfaces_server_option_ntp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


