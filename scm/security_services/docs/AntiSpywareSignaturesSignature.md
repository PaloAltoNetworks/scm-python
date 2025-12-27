# AntiSpywareSignaturesSignature

anti spyware signature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combination** | [**AntiSpywareSignaturesSignatureCombination**](AntiSpywareSignaturesSignatureCombination.md) |  | [optional] 
**standard** | [**List[AntiSpywareSignaturesSignatureStandardInner]**](AntiSpywareSignaturesSignatureStandardInner.md) |  | [optional] 

## Example

```python
from scm_security_services.models.anti_spyware_signatures_signature import AntiSpywareSignaturesSignature

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareSignaturesSignature from a JSON string
anti_spyware_signatures_signature_instance = AntiSpywareSignaturesSignature.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareSignaturesSignature.to_json())

# convert the object into a dict
anti_spyware_signatures_signature_dict = anti_spyware_signatures_signature_instance.to_dict()
# create an instance of AntiSpywareSignaturesSignature from a dict
anti_spyware_signatures_signature_from_dict = AntiSpywareSignaturesSignature.from_dict(anti_spyware_signatures_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


