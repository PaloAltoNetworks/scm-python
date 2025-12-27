# DnsSecurityProfilesBotnetDomainsSinkhole

DNS sinkhole settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_address** | **str** |  | [optional] 
**ipv6_address** | **str** |  | [optional] 

## Example

```python
from scm.security_services.models.dns_security_profiles_botnet_domains_sinkhole import DnsSecurityProfilesBotnetDomainsSinkhole

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecurityProfilesBotnetDomainsSinkhole from a JSON string
dns_security_profiles_botnet_domains_sinkhole_instance = DnsSecurityProfilesBotnetDomainsSinkhole.from_json(json)
# print the JSON string representation of the object
print(DnsSecurityProfilesBotnetDomainsSinkhole.to_json())

# convert the object into a dict
dns_security_profiles_botnet_domains_sinkhole_dict = dns_security_profiles_botnet_domains_sinkhole_instance.to_dict()
# create an instance of DnsSecurityProfilesBotnetDomainsSinkhole from a dict
dns_security_profiles_botnet_domains_sinkhole_from_dict = DnsSecurityProfilesBotnetDomainsSinkhole.from_dict(dns_security_profiles_botnet_domains_sinkhole_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


