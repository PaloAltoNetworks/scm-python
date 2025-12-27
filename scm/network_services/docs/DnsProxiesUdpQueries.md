# DnsProxiesUdpQueries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retries** | [**DnsProxiesUdpQueriesRetries**](DnsProxiesUdpQueriesRetries.md) |  | [optional] 

## Example

```python
from scm.network_services.models.dns_proxies_udp_queries import DnsProxiesUdpQueries

# TODO update the JSON string below
json = "{}"
# create an instance of DnsProxiesUdpQueries from a JSON string
dns_proxies_udp_queries_instance = DnsProxiesUdpQueries.from_json(json)
# print the JSON string representation of the object
print(DnsProxiesUdpQueries.to_json())

# convert the object into a dict
dns_proxies_udp_queries_dict = dns_proxies_udp_queries_instance.to_dict()
# create an instance of DnsProxiesUdpQueries from a dict
dns_proxies_udp_queries_from_dict = DnsProxiesUdpQueries.from_dict(dns_proxies_udp_queries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


