# DhcpInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Interface name | 
**relay** | [**DhcpInterfacesRelay**](DhcpInterfacesRelay.md) |  | [optional] 
**server** | [**DhcpInterfacesServer**](DhcpInterfacesServer.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.network_services.models.dhcp_interfaces import DhcpInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfaces from a JSON string
dhcp_interfaces_instance = DhcpInterfaces.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfaces.to_json())

# convert the object into a dict
dhcp_interfaces_dict = dhcp_interfaces_instance.to_dict()
# create an instance of DhcpInterfaces from a dict
dhcp_interfaces_from_dict = DhcpInterfaces.from_dict(dhcp_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


