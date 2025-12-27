# ScepProfilesCertificateAttributes

Subject Alternative name type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsname** | **str** |  | [optional] 
**rfc822name** | **str** |  | [optional] 
**uniform_resource_identifier** | **str** |  | [optional] 

## Example

```python
from scm.identity_services.models.scep_profiles_certificate_attributes import ScepProfilesCertificateAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ScepProfilesCertificateAttributes from a JSON string
scep_profiles_certificate_attributes_instance = ScepProfilesCertificateAttributes.from_json(json)
# print the JSON string representation of the object
print(ScepProfilesCertificateAttributes.to_json())

# convert the object into a dict
scep_profiles_certificate_attributes_dict = scep_profiles_certificate_attributes_instance.to_dict()
# create an instance of ScepProfilesCertificateAttributes from a dict
scep_profiles_certificate_attributes_from_dict = ScepProfilesCertificateAttributes.from_dict(scep_profiles_certificate_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


