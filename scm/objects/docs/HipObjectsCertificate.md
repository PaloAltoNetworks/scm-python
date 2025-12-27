# HipObjectsCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | [**HipObjectsCertificateCriteria**](HipObjectsCertificateCriteria.md) |  | [optional] 

## Example

```python
from scm_objects.models.hip_objects_certificate import HipObjectsCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsCertificate from a JSON string
hip_objects_certificate_instance = HipObjectsCertificate.from_json(json)
# print the JSON string representation of the object
print(HipObjectsCertificate.to_json())

# convert the object into a dict
hip_objects_certificate_dict = hip_objects_certificate_instance.to_dict()
# create an instance of HipObjectsCertificate from a dict
hip_objects_certificate_from_dict = HipObjectsCertificate.from_dict(hip_objects_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


