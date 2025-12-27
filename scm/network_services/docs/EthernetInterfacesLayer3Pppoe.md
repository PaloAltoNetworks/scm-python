# EthernetInterfacesLayer3Pppoe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_concentrator** | **str** | Access concentrator | [optional] 
**authentication** | **str** | Authentication protocol | [optional] 
**default_route_metric** | **int** | Metric of the default route created | [optional] [default to 10]
**enable** | **bool** |  | [optional] [default to True]
**passive** | [**EthernetInterfacesLayer3PppoePassive**](EthernetInterfacesLayer3PppoePassive.md) |  | [optional] 
**password** | **str** | Password | 
**service** | **str** | Service | [optional] 
**static_address** | [**EthernetInterfacesLayer3PppoeStaticAddress**](EthernetInterfacesLayer3PppoeStaticAddress.md) |  | [optional] 
**username** | **str** | Username | 

## Example

```python
from scm_network_services.models.ethernet_interfaces_layer3_pppoe import EthernetInterfacesLayer3Pppoe

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfacesLayer3Pppoe from a JSON string
ethernet_interfaces_layer3_pppoe_instance = EthernetInterfacesLayer3Pppoe.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfacesLayer3Pppoe.to_json())

# convert the object into a dict
ethernet_interfaces_layer3_pppoe_dict = ethernet_interfaces_layer3_pppoe_instance.to_dict()
# create an instance of EthernetInterfacesLayer3Pppoe from a dict
ethernet_interfaces_layer3_pppoe_from_dict = EthernetInterfacesLayer3Pppoe.from_dict(ethernet_interfaces_layer3_pppoe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


