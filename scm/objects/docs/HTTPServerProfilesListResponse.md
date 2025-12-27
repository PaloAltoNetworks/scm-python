# HTTPServerProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HttpServerProfiles]**](HttpServerProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.objects.models.http_server_profiles_list_response import HTTPServerProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPServerProfilesListResponse from a JSON string
http_server_profiles_list_response_instance = HTTPServerProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(HTTPServerProfilesListResponse.to_json())

# convert the object into a dict
http_server_profiles_list_response_dict = http_server_profiles_list_response_instance.to_dict()
# create an instance of HTTPServerProfilesListResponse from a dict
http_server_profiles_list_response_from_dict = HTTPServerProfilesListResponse.from_dict(http_server_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


