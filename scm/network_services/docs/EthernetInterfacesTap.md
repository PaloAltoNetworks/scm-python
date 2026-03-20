# EthernetInterfacesTap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**netflow_profile** | **str** | Name of Netflow Profile to assign to Interface | [optional] 

## Example

```python
from scm.network_services.models.ethernet_interfaces_tap import EthernetInterfacesTap

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfacesTap from a JSON string
ethernet_interfaces_tap_instance = EthernetInterfacesTap.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfacesTap.to_json())

# convert the object into a dict
ethernet_interfaces_tap_dict = ethernet_interfaces_tap_instance.to_dict()
# create an instance of EthernetInterfacesTap from a dict
ethernet_interfaces_tap_from_dict = EthernetInterfacesTap.from_dict(ethernet_interfaces_tap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


