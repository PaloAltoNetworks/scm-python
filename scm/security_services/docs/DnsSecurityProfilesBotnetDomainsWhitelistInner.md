# DnsSecurityProfilesBotnetDomainsWhitelistInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** | DNS domain or FQDN to be whitelisted | 

## Example

```python
from scm.security_services.models.dns_security_profiles_botnet_domains_whitelist_inner import DnsSecurityProfilesBotnetDomainsWhitelistInner

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecurityProfilesBotnetDomainsWhitelistInner from a JSON string
dns_security_profiles_botnet_domains_whitelist_inner_instance = DnsSecurityProfilesBotnetDomainsWhitelistInner.from_json(json)
# print the JSON string representation of the object
print(DnsSecurityProfilesBotnetDomainsWhitelistInner.to_json())

# convert the object into a dict
dns_security_profiles_botnet_domains_whitelist_inner_dict = dns_security_profiles_botnet_domains_whitelist_inner_instance.to_dict()
# create an instance of DnsSecurityProfilesBotnetDomainsWhitelistInner from a dict
dns_security_profiles_botnet_domains_whitelist_inner_from_dict = DnsSecurityProfilesBotnetDomainsWhitelistInner.from_dict(dns_security_profiles_botnet_domains_whitelist_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


