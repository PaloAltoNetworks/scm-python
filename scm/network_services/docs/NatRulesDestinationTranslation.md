# NatRulesDestinationTranslation

Destination translation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_rewrite** | [**NatRulesDestinationTranslationDnsRewrite**](NatRulesDestinationTranslationDnsRewrite.md) |  | [optional] 
**translated_address** | **str** | Translated destination IP address | [optional] 
**translated_port** | **int** | Translated destination port | [optional] 

## Example

```python
from scm.network_services.models.nat_rules_destination_translation import NatRulesDestinationTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of NatRulesDestinationTranslation from a JSON string
nat_rules_destination_translation_instance = NatRulesDestinationTranslation.from_json(json)
# print the JSON string representation of the object
print(NatRulesDestinationTranslation.to_json())

# convert the object into a dict
nat_rules_destination_translation_dict = nat_rules_destination_translation_instance.to_dict()
# create an instance of NatRulesDestinationTranslation from a dict
nat_rules_destination_translation_from_dict = NatRulesDestinationTranslation.from_dict(nat_rules_destination_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


