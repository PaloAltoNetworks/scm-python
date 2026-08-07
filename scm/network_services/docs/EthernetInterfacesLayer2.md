# EthernetInterfacesLayer2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lldp** | [**Lldp**](Lldp.md) |  | [optional] 
**netflow_profile** | **str** | Name of Netflow Profile to assign to Interface | [optional] 
**vlan_tag** | **str** | Assign interface to VLAN tag | [optional] 

## Example

```python
from scm.network_services.models.ethernet_interfaces_layer2 import EthernetInterfacesLayer2

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfacesLayer2 from a JSON string
ethernet_interfaces_layer2_instance = EthernetInterfacesLayer2.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfacesLayer2.to_json())

# convert the object into a dict
ethernet_interfaces_layer2_dict = ethernet_interfaces_layer2_instance.to_dict()
# create an instance of EthernetInterfacesLayer2 from a dict
ethernet_interfaces_layer2_from_dict = EthernetInterfacesLayer2.from_dict(ethernet_interfaces_layer2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


