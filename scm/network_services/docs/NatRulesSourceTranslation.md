# NatRulesSourceTranslation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_ip** | [**NatRulesSourceTranslationDynamicIp**](NatRulesSourceTranslationDynamicIp.md) |  | [optional] 
**dynamic_ip_and_port** | [**NatRulesSourceTranslationDynamicIpAndPort**](NatRulesSourceTranslationDynamicIpAndPort.md) |  | [optional] 
**static_ip** | [**NatRulesSourceTranslationStaticIp**](NatRulesSourceTranslationStaticIp.md) |  | [optional] 

## Example

```python
from scm_network_services.models.nat_rules_source_translation import NatRulesSourceTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of NatRulesSourceTranslation from a JSON string
nat_rules_source_translation_instance = NatRulesSourceTranslation.from_json(json)
# print the JSON string representation of the object
print(NatRulesSourceTranslation.to_json())

# convert the object into a dict
nat_rules_source_translation_dict = nat_rules_source_translation_instance.to_dict()
# create an instance of NatRulesSourceTranslation from a dict
nat_rules_source_translation_from_dict = NatRulesSourceTranslation.from_dict(nat_rules_source_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


