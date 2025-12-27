# NatRulesSourceTranslationStaticIp

Static IP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bi_directional** | **str** |  | [optional] 
**translated_address** | **str** | Translated IP address | [optional] 

## Example

```python
from scm.network_services.models.nat_rules_source_translation_static_ip import NatRulesSourceTranslationStaticIp

# TODO update the JSON string below
json = "{}"
# create an instance of NatRulesSourceTranslationStaticIp from a JSON string
nat_rules_source_translation_static_ip_instance = NatRulesSourceTranslationStaticIp.from_json(json)
# print the JSON string representation of the object
print(NatRulesSourceTranslationStaticIp.to_json())

# convert the object into a dict
nat_rules_source_translation_static_ip_dict = nat_rules_source_translation_static_ip_instance.to_dict()
# create an instance of NatRulesSourceTranslationStaticIp from a dict
nat_rules_source_translation_static_ip_from_dict = NatRulesSourceTranslationStaticIp.from_dict(nat_rules_source_translation_static_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


