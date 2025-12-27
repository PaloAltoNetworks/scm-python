# AggEthernetDhcpClient

Aggregate Ethernet DHCP Client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_client** | [**AggEthernetDhcpClientDhcpClient**](AggEthernetDhcpClientDhcpClient.md) |  | [optional] 

## Example

```python
from scm.network_services.models.agg_ethernet_dhcp_client import AggEthernetDhcpClient

# TODO update the JSON string below
json = "{}"
# create an instance of AggEthernetDhcpClient from a JSON string
agg_ethernet_dhcp_client_instance = AggEthernetDhcpClient.from_json(json)
# print the JSON string representation of the object
print(AggEthernetDhcpClient.to_json())

# convert the object into a dict
agg_ethernet_dhcp_client_dict = agg_ethernet_dhcp_client_instance.to_dict()
# create an instance of AggEthernetDhcpClient from a dict
agg_ethernet_dhcp_client_from_dict = AggEthernetDhcpClient.from_dict(agg_ethernet_dhcp_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


