# DnsProxies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache** | [**DnsProxiesCache**](DnsProxiesCache.md) |  | [optional] 
**default** | [**DnsProxiesDefault**](DnsProxiesDefault.md) |  | 
**device** | **str** | The device in which the resource is defined | [optional] 
**domain_servers** | [**List[DnsProxiesDomainServersInner]**](DnsProxiesDomainServersInner.md) | DNS proxy rules | [optional] 
**enabled** | **bool** | Enable DNS proxy? | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**interface** | **List[str]** | Interfaces on which to enable DNS proxy service | [optional] 
**name** | **str** | DNS proxy name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**static_entries** | [**List[DnsProxiesStaticEntriesInner]**](DnsProxiesStaticEntriesInner.md) |  | [optional] 
**tcp_queries** | [**DnsProxiesTcpQueries**](DnsProxiesTcpQueries.md) |  | [optional] 
**udp_queries** | [**DnsProxiesUdpQueries**](DnsProxiesUdpQueries.md) |  | [optional] 

## Example

```python
from scm_network_services.models.dns_proxies import DnsProxies

# TODO update the JSON string below
json = "{}"
# create an instance of DnsProxies from a JSON string
dns_proxies_instance = DnsProxies.from_json(json)
# print the JSON string representation of the object
print(DnsProxies.to_json())

# convert the object into a dict
dns_proxies_dict = dns_proxies_instance.to_dict()
# create an instance of DnsProxies from a dict
dns_proxies_from_dict = DnsProxies.from_dict(dns_proxies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


