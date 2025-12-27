# ApplicationsSignatureInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**and_condition** | [**List[ApplicationsSignatureInnerAndConditionInner]**](ApplicationsSignatureInnerAndConditionInner.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**name** | **str** | Alphanumeric string [ 0-9a-zA-Z._-] | 
**order_free** | **bool** |  | [optional] [default to False]
**scope** | **str** |  | [optional] [default to 'protocol-data-unit']

## Example

```python
from scm_objects.models.applications_signature_inner import ApplicationsSignatureInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsSignatureInner from a JSON string
applications_signature_inner_instance = ApplicationsSignatureInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationsSignatureInner.to_json())

# convert the object into a dict
applications_signature_inner_dict = applications_signature_inner_instance.to_dict()
# create an instance of ApplicationsSignatureInner from a dict
applications_signature_inner_from_dict = ApplicationsSignatureInner.from_dict(applications_signature_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


