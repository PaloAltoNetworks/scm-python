# DhcpInterfacesServerOptionWins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | Primary WINS server | [optional] 
**secondary** | **str** | Secondary WINS server | [optional] 

## Example

```python
from scm_network_services.models.dhcp_interfaces_server_option_wins import DhcpInterfacesServerOptionWins

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesServerOptionWins from a JSON string
dhcp_interfaces_server_option_wins_instance = DhcpInterfacesServerOptionWins.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesServerOptionWins.to_json())

# convert the object into a dict
dhcp_interfaces_server_option_wins_dict = dhcp_interfaces_server_option_wins_instance.to_dict()
# create an instance of DhcpInterfacesServerOptionWins from a dict
dhcp_interfaces_server_option_wins_from_dict = DhcpInterfacesServerOptionWins.from_dict(dhcp_interfaces_server_option_wins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


