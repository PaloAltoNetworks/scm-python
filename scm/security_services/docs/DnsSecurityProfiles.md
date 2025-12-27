# DnsSecurityProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**botnet_domains** | [**DnsSecurityProfilesBotnetDomains**](DnsSecurityProfilesBotnetDomains.md) |  | [optional] 
**description** | **str** | The description of the DNS security profile | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the DNS security profile | [optional] [readonly] 
**name** | **str** | The name of the DNS security profile | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.security_services.models.dns_security_profiles import DnsSecurityProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecurityProfiles from a JSON string
dns_security_profiles_instance = DnsSecurityProfiles.from_json(json)
# print the JSON string representation of the object
print(DnsSecurityProfiles.to_json())

# convert the object into a dict
dns_security_profiles_dict = dns_security_profiles_instance.to_dict()
# create an instance of DnsSecurityProfiles from a dict
dns_security_profiles_from_dict = DnsSecurityProfiles.from_dict(dns_security_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


