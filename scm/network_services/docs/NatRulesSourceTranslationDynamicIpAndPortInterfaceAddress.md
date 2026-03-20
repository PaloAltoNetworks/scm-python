# NatRulesSourceTranslationDynamicIpAndPortInterfaceAddress

Translated source interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floating_ip** | **str** | Floating IP address | [optional] 
**interface** | **str** | Interface name | [optional] 
**ip** | **str** | Translated source IP address | [optional] 

## Example

```python
from scm.network_services.models.nat_rules_source_translation_dynamic_ip_and_port_interface_address import NatRulesSourceTranslationDynamicIpAndPortInterfaceAddress

# TODO update the JSON string below
json = "{}"
# create an instance of NatRulesSourceTranslationDynamicIpAndPortInterfaceAddress from a JSON string
nat_rules_source_translation_dynamic_ip_and_port_interface_address_instance = NatRulesSourceTranslationDynamicIpAndPortInterfaceAddress.from_json(json)
# print the JSON string representation of the object
print(NatRulesSourceTranslationDynamicIpAndPortInterfaceAddress.to_json())

# convert the object into a dict
nat_rules_source_translation_dynamic_ip_and_port_interface_address_dict = nat_rules_source_translation_dynamic_ip_and_port_interface_address_instance.to_dict()
# create an instance of NatRulesSourceTranslationDynamicIpAndPortInterfaceAddress from a dict
nat_rules_source_translation_dynamic_ip_and_port_interface_address_from_dict = NatRulesSourceTranslationDynamicIpAndPortInterfaceAddress.from_dict(nat_rules_source_translation_dynamic_ip_and_port_interface_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


