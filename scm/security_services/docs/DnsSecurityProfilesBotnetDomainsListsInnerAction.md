# DnsSecurityProfilesBotnetDomainsListsInnerAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **object** |  | [optional] 
**allow** | **object** |  | [optional] 
**block** | **object** |  | [optional] 
**sinkhole** | **object** |  | [optional] 

## Example

```python
from scm_security_services.models.dns_security_profiles_botnet_domains_lists_inner_action import DnsSecurityProfilesBotnetDomainsListsInnerAction

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecurityProfilesBotnetDomainsListsInnerAction from a JSON string
dns_security_profiles_botnet_domains_lists_inner_action_instance = DnsSecurityProfilesBotnetDomainsListsInnerAction.from_json(json)
# print the JSON string representation of the object
print(DnsSecurityProfilesBotnetDomainsListsInnerAction.to_json())

# convert the object into a dict
dns_security_profiles_botnet_domains_lists_inner_action_dict = dns_security_profiles_botnet_domains_lists_inner_action_instance.to_dict()
# create an instance of DnsSecurityProfilesBotnetDomainsListsInnerAction from a dict
dns_security_profiles_botnet_domains_lists_inner_action_from_dict = DnsSecurityProfilesBotnetDomainsListsInnerAction.from_dict(dns_security_profiles_botnet_domains_lists_inner_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


