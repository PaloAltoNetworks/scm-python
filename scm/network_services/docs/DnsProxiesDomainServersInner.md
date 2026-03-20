# DnsProxiesDomainServersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cacheable** | **bool** | Enable caching for this DNS proxy rule? | [optional] 
**domain_name** | **List[str]** | Domain names(s) that will be matched | [optional] 
**name** | **str** | Proxy rule name | 
**primary** | **str** | Primary DNS server IP address | 
**secondary** | **str** | Secondary DNS server IP address | [optional] 

## Example

```python
from scm.network_services.models.dns_proxies_domain_servers_inner import DnsProxiesDomainServersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DnsProxiesDomainServersInner from a JSON string
dns_proxies_domain_servers_inner_instance = DnsProxiesDomainServersInner.from_json(json)
# print the JSON string representation of the object
print(DnsProxiesDomainServersInner.to_json())

# convert the object into a dict
dns_proxies_domain_servers_inner_dict = dns_proxies_domain_servers_inner_instance.to_dict()
# create an instance of DnsProxiesDomainServersInner from a dict
dns_proxies_domain_servers_inner_from_dict = DnsProxiesDomainServersInner.from_dict(dns_proxies_domain_servers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


