# AggEthernetDhcpClientDhcpClientSendHostname

Aggregate Ethernet DHCP Client Send hostname

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] [default to True]
**hostname** | **str** | Set interface hostname | [optional] [default to 'system-hostname']

## Example

```python
from scm_network_services.models.agg_ethernet_dhcp_client_dhcp_client_send_hostname import AggEthernetDhcpClientDhcpClientSendHostname

# TODO update the JSON string below
json = "{}"
# create an instance of AggEthernetDhcpClientDhcpClientSendHostname from a JSON string
agg_ethernet_dhcp_client_dhcp_client_send_hostname_instance = AggEthernetDhcpClientDhcpClientSendHostname.from_json(json)
# print the JSON string representation of the object
print(AggEthernetDhcpClientDhcpClientSendHostname.to_json())

# convert the object into a dict
agg_ethernet_dhcp_client_dhcp_client_send_hostname_dict = agg_ethernet_dhcp_client_dhcp_client_send_hostname_instance.to_dict()
# create an instance of AggEthernetDhcpClientDhcpClientSendHostname from a dict
agg_ethernet_dhcp_client_dhcp_client_send_hostname_from_dict = AggEthernetDhcpClientDhcpClientSendHostname.from_dict(agg_ethernet_dhcp_client_dhcp_client_send_hostname_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


