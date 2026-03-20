# AntiSpywareSignaturesSignatureStandardInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**and_condition** | [**List[AntiSpywareSignaturesSignatureStandardInnerAndConditionInner]**](AntiSpywareSignaturesSignatureStandardInnerAndConditionInner.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**name** | **str** |  | 
**order_free** | **bool** |  | [optional] [default to False]
**scope** | **str** |  | [optional] 

## Example

```python
from scm.security_services.models.anti_spyware_signatures_signature_standard_inner import AntiSpywareSignaturesSignatureStandardInner

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareSignaturesSignatureStandardInner from a JSON string
anti_spyware_signatures_signature_standard_inner_instance = AntiSpywareSignaturesSignatureStandardInner.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareSignaturesSignatureStandardInner.to_json())

# convert the object into a dict
anti_spyware_signatures_signature_standard_inner_dict = anti_spyware_signatures_signature_standard_inner_instance.to_dict()
# create an instance of AntiSpywareSignaturesSignatureStandardInner from a dict
anti_spyware_signatures_signature_standard_inner_from_dict = AntiSpywareSignaturesSignatureStandardInner.from_dict(anti_spyware_signatures_signature_standard_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


