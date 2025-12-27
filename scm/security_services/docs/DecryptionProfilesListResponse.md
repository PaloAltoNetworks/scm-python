# DecryptionProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DecryptionProfiles]**](DecryptionProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.security_services.models.decryption_profiles_list_response import DecryptionProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionProfilesListResponse from a JSON string
decryption_profiles_list_response_instance = DecryptionProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(DecryptionProfilesListResponse.to_json())

# convert the object into a dict
decryption_profiles_list_response_dict = decryption_profiles_list_response_instance.to_dict()
# create an instance of DecryptionProfilesListResponse from a dict
decryption_profiles_list_response_from_dict = DecryptionProfilesListResponse.from_dict(decryption_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


