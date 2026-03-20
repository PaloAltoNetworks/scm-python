# HTTPHeaderProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HttpHeaderProfiles]**](HttpHeaderProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.security_services.models.http_header_profiles_list_response import HTTPHeaderProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPHeaderProfilesListResponse from a JSON string
http_header_profiles_list_response_instance = HTTPHeaderProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(HTTPHeaderProfilesListResponse.to_json())

# convert the object into a dict
http_header_profiles_list_response_dict = http_header_profiles_list_response_instance.to_dict()
# create an instance of HTTPHeaderProfilesListResponse from a dict
http_header_profiles_list_response_from_dict = HTTPHeaderProfilesListResponse.from_dict(http_header_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


