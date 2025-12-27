# NatRulesSourceTranslationDynamicIpAndPort

Dynamic IP and port

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_address** | [**NatRulesSourceTranslationDynamicIpAndPortInterfaceAddress**](NatRulesSourceTranslationDynamicIpAndPortInterfaceAddress.md) |  | [optional] 
**translated_address** | **List[str]** | Translated source IP addresses | [optional] 

## Example

```python
from scm.network_services.models.nat_rules_source_translation_dynamic_ip_and_port import NatRulesSourceTranslationDynamicIpAndPort

# TODO update the JSON string below
json = "{}"
# create an instance of NatRulesSourceTranslationDynamicIpAndPort from a JSON string
nat_rules_source_translation_dynamic_ip_and_port_instance = NatRulesSourceTranslationDynamicIpAndPort.from_json(json)
# print the JSON string representation of the object
print(NatRulesSourceTranslationDynamicIpAndPort.to_json())

# convert the object into a dict
nat_rules_source_translation_dynamic_ip_and_port_dict = nat_rules_source_translation_dynamic_ip_and_port_instance.to_dict()
# create an instance of NatRulesSourceTranslationDynamicIpAndPort from a dict
nat_rules_source_translation_dynamic_ip_and_port_from_dict = NatRulesSourceTranslationDynamicIpAndPort.from_dict(nat_rules_source_translation_dynamic_ip_and_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


