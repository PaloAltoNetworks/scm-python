# AntiSpywareSignaturesSignatureCombinationAndConditionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**or_condition** | [**List[AntiSpywareSignaturesSignatureCombinationAndConditionInnerOrConditionInner]**](AntiSpywareSignaturesSignatureCombinationAndConditionInnerOrConditionInner.md) |  | [optional] 

## Example

```python
from scm_security_services.models.anti_spyware_signatures_signature_combination_and_condition_inner import AntiSpywareSignaturesSignatureCombinationAndConditionInner

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareSignaturesSignatureCombinationAndConditionInner from a JSON string
anti_spyware_signatures_signature_combination_and_condition_inner_instance = AntiSpywareSignaturesSignatureCombinationAndConditionInner.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareSignaturesSignatureCombinationAndConditionInner.to_json())

# convert the object into a dict
anti_spyware_signatures_signature_combination_and_condition_inner_dict = anti_spyware_signatures_signature_combination_and_condition_inner_instance.to_dict()
# create an instance of AntiSpywareSignaturesSignatureCombinationAndConditionInner from a dict
anti_spyware_signatures_signature_combination_and_condition_inner_from_dict = AntiSpywareSignaturesSignatureCombinationAndConditionInner.from_dict(anti_spyware_signatures_signature_combination_and_condition_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


