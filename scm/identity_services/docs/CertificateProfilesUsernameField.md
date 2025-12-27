# CertificateProfilesUsernameField

Certificate username field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Common name | [optional] 
**subject_alt** | **str** | Email address | [optional] 

## Example

```python
from scm.identity_services.models.certificate_profiles_username_field import CertificateProfilesUsernameField

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateProfilesUsernameField from a JSON string
certificate_profiles_username_field_instance = CertificateProfilesUsernameField.from_json(json)
# print the JSON string representation of the object
print(CertificateProfilesUsernameField.to_json())

# convert the object into a dict
certificate_profiles_username_field_dict = certificate_profiles_username_field_instance.to_dict()
# create an instance of CertificateProfilesUsernameField from a dict
certificate_profiles_username_field_from_dict = CertificateProfilesUsernameField.from_dict(certificate_profiles_username_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


