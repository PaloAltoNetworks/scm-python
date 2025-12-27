# DnsProxiesCache


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_edns** | **bool** | Cache EDNS UDP response | [optional] [default to True]
**enabled** | **bool** | Turn on caching for this DNS object | [default to True]
**max_ttl** | [**DnsProxiesCacheMaxTtl**](DnsProxiesCacheMaxTtl.md) |  | [optional] 

## Example

```python
from scm_network_services.models.dns_proxies_cache import DnsProxiesCache

# TODO update the JSON string below
json = "{}"
# create an instance of DnsProxiesCache from a JSON string
dns_proxies_cache_instance = DnsProxiesCache.from_json(json)
# print the JSON string representation of the object
print(DnsProxiesCache.to_json())

# convert the object into a dict
dns_proxies_cache_dict = dns_proxies_cache_instance.to_dict()
# create an instance of DnsProxiesCache from a dict
dns_proxies_cache_from_dict = DnsProxiesCache.from_dict(dns_proxies_cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


