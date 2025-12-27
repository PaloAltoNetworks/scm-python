# DnsProxiesUdpQueriesRetries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | **int** | Maximum number of retries before trying next name server | [optional] [default to 5]
**interval** | **int** | Time in seconds for another request to be sent | [optional] [default to 2]

## Example

```python
from scm_network_services.models.dns_proxies_udp_queries_retries import DnsProxiesUdpQueriesRetries

# TODO update the JSON string below
json = "{}"
# create an instance of DnsProxiesUdpQueriesRetries from a JSON string
dns_proxies_udp_queries_retries_instance = DnsProxiesUdpQueriesRetries.from_json(json)
# print the JSON string representation of the object
print(DnsProxiesUdpQueriesRetries.to_json())

# convert the object into a dict
dns_proxies_udp_queries_retries_dict = dns_proxies_udp_queries_retries_instance.to_dict()
# create an instance of DnsProxiesUdpQueriesRetries from a dict
dns_proxies_udp_queries_retries_from_dict = DnsProxiesUdpQueriesRetries.from_dict(dns_proxies_udp_queries_retries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


