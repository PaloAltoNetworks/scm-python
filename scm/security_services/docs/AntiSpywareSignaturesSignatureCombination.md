# AntiSpywareSignaturesSignatureCombination

anti spyware signature combination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**and_condition** | [**List[AntiSpywareSignaturesSignatureCombinationAndConditionInner]**](AntiSpywareSignaturesSignatureCombinationAndConditionInner.md) |  | [optional] 
**order_free** | **bool** |  | [optional] [default to False]
**time_attribute** | [**AntiSpywareSignaturesSignatureCombinationTimeAttribute**](AntiSpywareSignaturesSignatureCombinationTimeAttribute.md) |  | [optional] 

## Example

```python
from scm_security_services.models.anti_spyware_signatures_signature_combination import AntiSpywareSignaturesSignatureCombination

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareSignaturesSignatureCombination from a JSON string
anti_spyware_signatures_signature_combination_instance = AntiSpywareSignaturesSignatureCombination.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareSignaturesSignatureCombination.to_json())

# convert the object into a dict
anti_spyware_signatures_signature_combination_dict = anti_spyware_signatures_signature_combination_instance.to_dict()
# create an instance of AntiSpywareSignaturesSignatureCombination from a dict
anti_spyware_signatures_signature_combination_from_dict = AntiSpywareSignaturesSignatureCombination.from_dict(anti_spyware_signatures_signature_combination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


