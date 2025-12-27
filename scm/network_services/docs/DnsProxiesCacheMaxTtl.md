# DnsProxiesCacheMaxTtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable max ttl for this DNS object | [default to False]
**time_to_live** | **int** | Time in seconds after which entry is cleared | [optional] 

## Example

```python
from scm_network_services.models.dns_proxies_cache_max_ttl import DnsProxiesCacheMaxTtl

# TODO update the JSON string below
json = "{}"
# create an instance of DnsProxiesCacheMaxTtl from a JSON string
dns_proxies_cache_max_ttl_instance = DnsProxiesCacheMaxTtl.from_json(json)
# print the JSON string representation of the object
print(DnsProxiesCacheMaxTtl.to_json())

# convert the object into a dict
dns_proxies_cache_max_ttl_dict = dns_proxies_cache_max_ttl_instance.to_dict()
# create an instance of DnsProxiesCacheMaxTtl from a dict
dns_proxies_cache_max_ttl_from_dict = DnsProxiesCacheMaxTtl.from_dict(dns_proxies_cache_max_ttl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


