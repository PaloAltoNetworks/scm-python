# DnsProxiesStaticEntriesInner

Static domain name mappings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **List[str]** |  | 
**domain** | **str** | Fully qualified domain name | 
**name** | **str** | Static entry name | 

## Example

```python
from scm.network_services.models.dns_proxies_static_entries_inner import DnsProxiesStaticEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DnsProxiesStaticEntriesInner from a JSON string
dns_proxies_static_entries_inner_instance = DnsProxiesStaticEntriesInner.from_json(json)
# print the JSON string representation of the object
print(DnsProxiesStaticEntriesInner.to_json())

# convert the object into a dict
dns_proxies_static_entries_inner_dict = dns_proxies_static_entries_inner_instance.to_dict()
# create an instance of DnsProxiesStaticEntriesInner from a dict
dns_proxies_static_entries_inner_from_dict = DnsProxiesStaticEntriesInner.from_dict(dns_proxies_static_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


