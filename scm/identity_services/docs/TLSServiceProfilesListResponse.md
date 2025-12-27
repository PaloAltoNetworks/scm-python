# TLSServiceProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TlsServiceProfiles]**](TlsServiceProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_identity_services.models.tls_service_profiles_list_response import TLSServiceProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TLSServiceProfilesListResponse from a JSON string
tls_service_profiles_list_response_instance = TLSServiceProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(TLSServiceProfilesListResponse.to_json())

# convert the object into a dict
tls_service_profiles_list_response_dict = tls_service_profiles_list_response_instance.to_dict()
# create an instance of TLSServiceProfilesListResponse from a dict
tls_service_profiles_list_response_from_dict = TLSServiceProfilesListResponse.from_dict(tls_service_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


