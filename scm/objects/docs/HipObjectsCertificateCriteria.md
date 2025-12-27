# HipObjectsCertificateCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_attributes** | [**List[HipObjectsCertificateCriteriaCertificateAttributesInner]**](HipObjectsCertificateCriteriaCertificateAttributesInner.md) |  | [optional] 
**certificate_profile** | **str** | Profile for authenticating client certificates | [optional] 

## Example

```python
from scm_objects.models.hip_objects_certificate_criteria import HipObjectsCertificateCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsCertificateCriteria from a JSON string
hip_objects_certificate_criteria_instance = HipObjectsCertificateCriteria.from_json(json)
# print the JSON string representation of the object
print(HipObjectsCertificateCriteria.to_json())

# convert the object into a dict
hip_objects_certificate_criteria_dict = hip_objects_certificate_criteria_instance.to_dict()
# create an instance of HipObjectsCertificateCriteria from a dict
hip_objects_certificate_criteria_from_dict = HipObjectsCertificateCriteria.from_dict(hip_objects_certificate_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


