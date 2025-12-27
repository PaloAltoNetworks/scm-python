# NatRulesSourceTranslationDynamicIp

Dynamic IP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback** | [**NatRulesSourceTranslationDynamicIpFallback**](NatRulesSourceTranslationDynamicIpFallback.md) |  | [optional] 
**translated_address** | **List[str]** | Translated IP addresses | [optional] 

## Example

```python
from scm_network_services.models.nat_rules_source_translation_dynamic_ip import NatRulesSourceTranslationDynamicIp

# TODO update the JSON string below
json = "{}"
# create an instance of NatRulesSourceTranslationDynamicIp from a JSON string
nat_rules_source_translation_dynamic_ip_instance = NatRulesSourceTranslationDynamicIp.from_json(json)
# print the JSON string representation of the object
print(NatRulesSourceTranslationDynamicIp.to_json())

# convert the object into a dict
nat_rules_source_translation_dynamic_ip_dict = nat_rules_source_translation_dynamic_ip_instance.to_dict()
# create an instance of NatRulesSourceTranslationDynamicIp from a dict
nat_rules_source_translation_dynamic_ip_from_dict = NatRulesSourceTranslationDynamicIp.from_dict(nat_rules_source_translation_dynamic_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


