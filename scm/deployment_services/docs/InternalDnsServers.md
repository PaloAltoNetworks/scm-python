# InternalDnsServers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **List[str]** | The DNS domain name(s) | 
**id** | **str** | The UUID of the internet DNS server resource | [readonly] 
**name** | **str** | The name of the internet DNS server resource | 
**primary** | **str** | The IP address of the primary DNS server | 
**secondary** | **str** | The IP address of the secondary DNS server | [optional] 

## Example

```python
from scm.deployment_services.models.internal_dns_servers import InternalDnsServers

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDnsServers from a JSON string
internal_dns_servers_instance = InternalDnsServers.from_json(json)
# print the JSON string representation of the object
print(InternalDnsServers.to_json())

# convert the object into a dict
internal_dns_servers_dict = internal_dns_servers_instance.to_dict()
# create an instance of InternalDnsServers from a dict
internal_dns_servers_from_dict = InternalDnsServers.from_dict(internal_dns_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


