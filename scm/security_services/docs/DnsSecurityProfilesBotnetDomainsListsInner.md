# DnsSecurityProfilesBotnetDomainsListsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**DnsSecurityProfilesBotnetDomainsListsInnerAction**](DnsSecurityProfilesBotnetDomainsListsInnerAction.md) |  | [optional] 
**name** | **str** |  | 
**packet_capture** | **str** |  | [optional] 

## Example

```python
from scm.security_services.models.dns_security_profiles_botnet_domains_lists_inner import DnsSecurityProfilesBotnetDomainsListsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecurityProfilesBotnetDomainsListsInner from a JSON string
dns_security_profiles_botnet_domains_lists_inner_instance = DnsSecurityProfilesBotnetDomainsListsInner.from_json(json)
# print the JSON string representation of the object
print(DnsSecurityProfilesBotnetDomainsListsInner.to_json())

# convert the object into a dict
dns_security_profiles_botnet_domains_lists_inner_dict = dns_security_profiles_botnet_domains_lists_inner_instance.to_dict()
# create an instance of DnsSecurityProfilesBotnetDomainsListsInner from a dict
dns_security_profiles_botnet_domains_lists_inner_from_dict = DnsSecurityProfilesBotnetDomainsListsInner.from_dict(dns_security_profiles_botnet_domains_lists_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


