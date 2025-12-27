# ApplicationsSignatureInnerAndConditionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Alphanumeric string [ 0-9a-zA-Z._-] | 
**or_condition** | [**List[ApplicationsSignatureInnerAndConditionInnerOrConditionInner]**](ApplicationsSignatureInnerAndConditionInnerOrConditionInner.md) |  | [optional] 

## Example

```python
from scm.objects.models.applications_signature_inner_and_condition_inner import ApplicationsSignatureInnerAndConditionInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsSignatureInnerAndConditionInner from a JSON string
applications_signature_inner_and_condition_inner_instance = ApplicationsSignatureInnerAndConditionInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationsSignatureInnerAndConditionInner.to_json())

# convert the object into a dict
applications_signature_inner_and_condition_inner_dict = applications_signature_inner_and_condition_inner_instance.to_dict()
# create an instance of ApplicationsSignatureInnerAndConditionInner from a dict
applications_signature_inner_and_condition_inner_from_dict = ApplicationsSignatureInnerAndConditionInner.from_dict(applications_signature_inner_and_condition_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


