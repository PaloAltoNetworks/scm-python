# EthernetInterfacesLayer2Lldp

LLDP Settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable LLDP on Interface | [default to False]

## Example

```python
from scm.network_services.models.ethernet_interfaces_layer2_lldp import EthernetInterfacesLayer2Lldp

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfacesLayer2Lldp from a JSON string
ethernet_interfaces_layer2_lldp_instance = EthernetInterfacesLayer2Lldp.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfacesLayer2Lldp.to_json())

# convert the object into a dict
ethernet_interfaces_layer2_lldp_dict = ethernet_interfaces_layer2_lldp_instance.to_dict()
# create an instance of EthernetInterfacesLayer2Lldp from a dict
ethernet_interfaces_layer2_lldp_from_dict = EthernetInterfacesLayer2Lldp.from_dict(ethernet_interfaces_layer2_lldp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


