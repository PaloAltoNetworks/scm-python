# DnsSecurityProfilesBotnetDomains

Botnet domains

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_security_categories** | [**List[DnsSecurityProfilesBotnetDomainsDnsSecurityCategoriesInner]**](DnsSecurityProfilesBotnetDomainsDnsSecurityCategoriesInner.md) | DNS categories | [optional] 
**lists** | [**List[DnsSecurityProfilesBotnetDomainsListsInner]**](DnsSecurityProfilesBotnetDomainsListsInner.md) | Dynamic lists of DNS domains | [optional] 
**sinkhole** | [**DnsSecurityProfilesBotnetDomainsSinkhole**](DnsSecurityProfilesBotnetDomainsSinkhole.md) |  | [optional] 
**whitelist** | [**List[DnsSecurityProfilesBotnetDomainsWhitelistInner]**](DnsSecurityProfilesBotnetDomainsWhitelistInner.md) | DNS security overrides | [optional] 

## Example

```python
from scm.security_services.models.dns_security_profiles_botnet_domains import DnsSecurityProfilesBotnetDomains

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecurityProfilesBotnetDomains from a JSON string
dns_security_profiles_botnet_domains_instance = DnsSecurityProfilesBotnetDomains.from_json(json)
# print the JSON string representation of the object
print(DnsSecurityProfilesBotnetDomains.to_json())

# convert the object into a dict
dns_security_profiles_botnet_domains_dict = dns_security_profiles_botnet_domains_instance.to_dict()
# create an instance of DnsSecurityProfilesBotnetDomains from a dict
dns_security_profiles_botnet_domains_from_dict = DnsSecurityProfilesBotnetDomains.from_dict(dns_security_profiles_botnet_domains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


