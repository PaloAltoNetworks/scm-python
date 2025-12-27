# EthernetInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate_group** | **str** |  | [optional] 
**comment** | **str** | Interface description | [optional] 
**default_value** | **str** | Default interface assignment | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [readonly] 
**layer2** | [**EthernetInterfacesLayer2**](EthernetInterfacesLayer2.md) |  | [optional] 
**layer3** | [**EthernetInterfacesLayer3**](EthernetInterfacesLayer3.md) |  | [optional] 
**link_duplex** | **str** | Link duplex | [optional] [default to 'auto']
**link_speed** | **str** | Link speed | [optional] [default to 'auto']
**link_state** | **str** | Link state | [optional] [default to 'auto']
**name** | **str** | Interface name | 
**poe** | [**Poe**](Poe.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**tap** | **object** |  | [optional] 

## Example

```python
from scm_network_services.models.ethernet_interfaces import EthernetInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfaces from a JSON string
ethernet_interfaces_instance = EthernetInterfaces.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfaces.to_json())

# convert the object into a dict
ethernet_interfaces_dict = ethernet_interfaces_instance.to_dict()
# create an instance of EthernetInterfaces from a dict
ethernet_interfaces_from_dict = EthernetInterfaces.from_dict(ethernet_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


