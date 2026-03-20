# NatRulesSourceTranslationDynamicIpFallback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_address** | [**NatRulesSourceTranslationDynamicIpFallbackInterfaceAddress**](NatRulesSourceTranslationDynamicIpFallbackInterfaceAddress.md) |  | [optional] 
**translated_address** | **List[str]** | Fallback IP addresses | [optional] 

## Example

```python
from scm.network_services.models.nat_rules_source_translation_dynamic_ip_fallback import NatRulesSourceTranslationDynamicIpFallback

# TODO update the JSON string below
json = "{}"
# create an instance of NatRulesSourceTranslationDynamicIpFallback from a JSON string
nat_rules_source_translation_dynamic_ip_fallback_instance = NatRulesSourceTranslationDynamicIpFallback.from_json(json)
# print the JSON string representation of the object
print(NatRulesSourceTranslationDynamicIpFallback.to_json())

# convert the object into a dict
nat_rules_source_translation_dynamic_ip_fallback_dict = nat_rules_source_translation_dynamic_ip_fallback_instance.to_dict()
# create an instance of NatRulesSourceTranslationDynamicIpFallback from a dict
nat_rules_source_translation_dynamic_ip_fallback_from_dict = NatRulesSourceTranslationDynamicIpFallback.from_dict(nat_rules_source_translation_dynamic_ip_fallback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


