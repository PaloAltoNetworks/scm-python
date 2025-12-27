# AggEthernetDhcpClientDhcpClient

Aggregate Ethernet DHCP Client Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_default_route** | **bool** | Automatically create default route pointing to default gateway provided by server | [optional] [default to True]
**default_route_metric** | **int** | Metric of the default route created | [optional] [default to 10]
**enable** | **bool** | Enable DHCP? | [optional] [default to True]
**send_hostname** | [**AggEthernetDhcpClientDhcpClientSendHostname**](AggEthernetDhcpClientDhcpClientSendHostname.md) |  | [optional] 

## Example

```python
from scm.network_services.models.agg_ethernet_dhcp_client_dhcp_client import AggEthernetDhcpClientDhcpClient

# TODO update the JSON string below
json = "{}"
# create an instance of AggEthernetDhcpClientDhcpClient from a JSON string
agg_ethernet_dhcp_client_dhcp_client_instance = AggEthernetDhcpClientDhcpClient.from_json(json)
# print the JSON string representation of the object
print(AggEthernetDhcpClientDhcpClient.to_json())

# convert the object into a dict
agg_ethernet_dhcp_client_dhcp_client_dict = agg_ethernet_dhcp_client_dhcp_client_instance.to_dict()
# create an instance of AggEthernetDhcpClientDhcpClient from a dict
agg_ethernet_dhcp_client_dhcp_client_from_dict = AggEthernetDhcpClientDhcpClient.from_dict(agg_ethernet_dhcp_client_dhcp_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


