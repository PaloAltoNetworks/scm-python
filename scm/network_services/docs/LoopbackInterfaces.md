# LoopbackInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Description | [optional] 
**default_value** | **str** | Default interface assignment | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**interface_management_profile** | **str** | Interface management profile | [optional] 
**ip** | [**List[LoopbackInterfacesIpInner]**](LoopbackInterfacesIpInner.md) | Loopback IP Parent | [optional] 
**ipv6** | [**LoopbackInterfacesIpv6**](LoopbackInterfacesIpv6.md) |  | [optional] 
**mtu** | **int** | MTU | [optional] 
**name** | **str** | Loopback Interface name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.loopback_interfaces import LoopbackInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of LoopbackInterfaces from a JSON string
loopback_interfaces_instance = LoopbackInterfaces.from_json(json)
# print the JSON string representation of the object
print(LoopbackInterfaces.to_json())

# convert the object into a dict
loopback_interfaces_dict = loopback_interfaces_instance.to_dict()
# create an instance of LoopbackInterfaces from a dict
loopback_interfaces_from_dict = LoopbackInterfaces.from_dict(loopback_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


