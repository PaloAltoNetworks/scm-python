# DnsProxiesTcpQueries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Turn on forwarding of TCP DNS queries? | [default to False]
**max_pending_requests** | **int** | Upper limit on number of concurrent TCP DNS requests | [optional] [default to 64]

## Example

```python
from scm.network_services.models.dns_proxies_tcp_queries import DnsProxiesTcpQueries

# TODO update the JSON string below
json = "{}"
# create an instance of DnsProxiesTcpQueries from a JSON string
dns_proxies_tcp_queries_instance = DnsProxiesTcpQueries.from_json(json)
# print the JSON string representation of the object
print(DnsProxiesTcpQueries.to_json())

# convert the object into a dict
dns_proxies_tcp_queries_dict = dns_proxies_tcp_queries_instance.to_dict()
# create an instance of DnsProxiesTcpQueries from a dict
dns_proxies_tcp_queries_from_dict = DnsProxiesTcpQueries.from_dict(dns_proxies_tcp_queries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


