# NatRulesDynamicDestinationTranslation

Dynamic destination translation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distribution** | **str** | Distribution method | [optional] 
**translated_address** | **str** | Translated destination IP address | [optional] 
**translated_port** | **int** | Translated destination port | [optional] 

## Example

```python
from scm_network_services.models.nat_rules_dynamic_destination_translation import NatRulesDynamicDestinationTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of NatRulesDynamicDestinationTranslation from a JSON string
nat_rules_dynamic_destination_translation_instance = NatRulesDynamicDestinationTranslation.from_json(json)
# print the JSON string representation of the object
print(NatRulesDynamicDestinationTranslation.to_json())

# convert the object into a dict
nat_rules_dynamic_destination_translation_dict = nat_rules_dynamic_destination_translation_instance.to_dict()
# create an instance of NatRulesDynamicDestinationTranslation from a dict
nat_rules_dynamic_destination_translation_from_dict = NatRulesDynamicDestinationTranslation.from_dict(nat_rules_dynamic_destination_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


