# AggregateInterfacesLayer3

Aggregate Interface Layer 3 configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arp** | [**List[AggEthernetArpInner]**](AggEthernetArpInner.md) | Aggregate Ethernet ARP configuration | [optional] 
**ddns_config** | [**AggregateInterfacesLayer3DdnsConfig**](AggregateInterfacesLayer3DdnsConfig.md) |  | [optional] 
**dhcp_client** | [**AggEthernetDhcpClientDhcpClient**](AggEthernetDhcpClientDhcpClient.md) |  | [optional] 
**interface_management_profile** | **str** | Interface management profile | [optional] 
**ip** | [**List[AggregateInterfacesLayer3IpInner]**](AggregateInterfacesLayer3IpInner.md) | Aggregate Interface IP addresses | [optional] 
**lacp** | [**Lacp**](Lacp.md) |  | [optional] 
**mtu** | **int** | MTU | [optional] [default to 1500]

## Example

```python
from scm.network_services.models.aggregate_interfaces_layer3 import AggregateInterfacesLayer3

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateInterfacesLayer3 from a JSON string
aggregate_interfaces_layer3_instance = AggregateInterfacesLayer3.from_json(json)
# print the JSON string representation of the object
print(AggregateInterfacesLayer3.to_json())

# convert the object into a dict
aggregate_interfaces_layer3_dict = aggregate_interfaces_layer3_instance.to_dict()
# create an instance of AggregateInterfacesLayer3 from a dict
aggregate_interfaces_layer3_from_dict = AggregateInterfacesLayer3.from_dict(aggregate_interfaces_layer3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


