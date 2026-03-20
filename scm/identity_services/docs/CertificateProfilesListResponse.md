# CertificateProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CertificateProfiles]**](CertificateProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.identity_services.models.certificate_profiles_list_response import CertificateProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateProfilesListResponse from a JSON string
certificate_profiles_list_response_instance = CertificateProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(CertificateProfilesListResponse.to_json())

# convert the object into a dict
certificate_profiles_list_response_dict = certificate_profiles_list_response_instance.to_dict()
# create an instance of CertificateProfilesListResponse from a dict
certificate_profiles_list_response_from_dict = CertificateProfilesListResponse.from_dict(certificate_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


