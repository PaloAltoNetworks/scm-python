# NatRulesSourceTranslationDynamicIpFallbackInterfaceAddress

Fallback interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floating_ip** | **str** | Floating IP address | [optional] 
**interface** | **str** | Interface name | [optional] 
**ip** | **str** | IP address | [optional] 

## Example

```python
from scm.network_services.models.nat_rules_source_translation_dynamic_ip_fallback_interface_address import NatRulesSourceTranslationDynamicIpFallbackInterfaceAddress

# TODO update the JSON string below
json = "{}"
# create an instance of NatRulesSourceTranslationDynamicIpFallbackInterfaceAddress from a JSON string
nat_rules_source_translation_dynamic_ip_fallback_interface_address_instance = NatRulesSourceTranslationDynamicIpFallbackInterfaceAddress.from_json(json)
# print the JSON string representation of the object
print(NatRulesSourceTranslationDynamicIpFallbackInterfaceAddress.to_json())

# convert the object into a dict
nat_rules_source_translation_dynamic_ip_fallback_interface_address_dict = nat_rules_source_translation_dynamic_ip_fallback_interface_address_instance.to_dict()
# create an instance of NatRulesSourceTranslationDynamicIpFallbackInterfaceAddress from a dict
nat_rules_source_translation_dynamic_ip_fallback_interface_address_from_dict = NatRulesSourceTranslationDynamicIpFallbackInterfaceAddress.from_dict(nat_rules_source_translation_dynamic_ip_fallback_interface_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


