# DnsSecurityProfilesBotnetDomainsDnsSecurityCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] [default to 'default']
**log_level** | **str** |  | [optional] [default to 'default']
**name** | **str** |  | [optional] 
**packet_capture** | **str** |  | [optional] 

## Example

```python
from scm_security_services.models.dns_security_profiles_botnet_domains_dns_security_categories_inner import DnsSecurityProfilesBotnetDomainsDnsSecurityCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecurityProfilesBotnetDomainsDnsSecurityCategoriesInner from a JSON string
dns_security_profiles_botnet_domains_dns_security_categories_inner_instance = DnsSecurityProfilesBotnetDomainsDnsSecurityCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(DnsSecurityProfilesBotnetDomainsDnsSecurityCategoriesInner.to_json())

# convert the object into a dict
dns_security_profiles_botnet_domains_dns_security_categories_inner_dict = dns_security_profiles_botnet_domains_dns_security_categories_inner_instance.to_dict()
# create an instance of DnsSecurityProfilesBotnetDomainsDnsSecurityCategoriesInner from a dict
dns_security_profiles_botnet_domains_dns_security_categories_inner_from_dict = DnsSecurityProfilesBotnetDomainsDnsSecurityCategoriesInner.from_dict(dns_security_profiles_botnet_domains_dns_security_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


