# Addresses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the address object | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**fqdn** | **str** | Fully qualified domain name | [optional] 
**id** | **str** | The UUID of the address object | [readonly] 
**ip_netmask** | **str** | IP address with or without CIDR notation | [optional] 
**ip_range** | **str** |  | [optional] 
**ip_wildcard** | **str** | IP wildcard mask | [optional] 
**name** | **str** | The name of the address object | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**tag** | **List[str]** | Tags assocaited with the address object | [optional] 

## Example

```python
from scm.objects.models.addresses import Addresses

# TODO update the JSON string below
json = "{}"
# create an instance of Addresses from a JSON string
addresses_instance = Addresses.from_json(json)
# print the JSON string representation of the object
print(Addresses.to_json())

# convert the object into a dict
addresses_dict = addresses_instance.to_dict()
# create an instance of Addresses from a dict
addresses_from_dict = Addresses.from_dict(addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


