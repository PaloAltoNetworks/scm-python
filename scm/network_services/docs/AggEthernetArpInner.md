# AggEthernetArpInner

Aggregate Ethernet ARP configuration object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hw_address** | **str** | MAC address | [optional] 
**name** | **str** | IP address | [optional] 

## Example

```python
from scm_network_services.models.agg_ethernet_arp_inner import AggEthernetArpInner

# TODO update the JSON string below
json = "{}"
# create an instance of AggEthernetArpInner from a JSON string
agg_ethernet_arp_inner_instance = AggEthernetArpInner.from_json(json)
# print the JSON string representation of the object
print(AggEthernetArpInner.to_json())

# convert the object into a dict
agg_ethernet_arp_inner_dict = agg_ethernet_arp_inner_instance.to_dict()
# create an instance of AggEthernetArpInner from a dict
agg_ethernet_arp_inner_from_dict = AggEthernetArpInner.from_dict(agg_ethernet_arp_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


