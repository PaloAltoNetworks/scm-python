# DnsProxiesDefault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inheritance** | [**DnsProxiesDefaultInheritance**](DnsProxiesDefaultInheritance.md) |  | [optional] 
**primary** | **str** | Primary DNS Name server IP address | 
**secondary** | **str** | Secondary DNS Name server IP address | [optional] 

## Example

```python
from scm_network_services.models.dns_proxies_default import DnsProxiesDefault

# TODO update the JSON string below
json = "{}"
# create an instance of DnsProxiesDefault from a JSON string
dns_proxies_default_instance = DnsProxiesDefault.from_json(json)
# print the JSON string representation of the object
print(DnsProxiesDefault.to_json())

# convert the object into a dict
dns_proxies_default_dict = dns_proxies_default_instance.to_dict()
# create an instance of DnsProxiesDefault from a dict
dns_proxies_default_from_dict = DnsProxiesDefault.from_dict(dns_proxies_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


