# FileBlockingProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FileBlockingProfiles]**](FileBlockingProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.security_services.models.file_blocking_profiles_list_response import FileBlockingProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileBlockingProfilesListResponse from a JSON string
file_blocking_profiles_list_response_instance = FileBlockingProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(FileBlockingProfilesListResponse.to_json())

# convert the object into a dict
file_blocking_profiles_list_response_dict = file_blocking_profiles_list_response_instance.to_dict()
# create an instance of FileBlockingProfilesListResponse from a dict
file_blocking_profiles_list_response_from_dict = FileBlockingProfilesListResponse.from_dict(file_blocking_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


