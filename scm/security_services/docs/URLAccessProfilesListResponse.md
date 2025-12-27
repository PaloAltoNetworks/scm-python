# URLAccessProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UrlAccessProfiles]**](UrlAccessProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_security_services.models.url_access_profiles_list_response import URLAccessProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of URLAccessProfilesListResponse from a JSON string
url_access_profiles_list_response_instance = URLAccessProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(URLAccessProfilesListResponse.to_json())

# convert the object into a dict
url_access_profiles_list_response_dict = url_access_profiles_list_response_instance.to_dict()
# create an instance of URLAccessProfilesListResponse from a dict
url_access_profiles_list_response_from_dict = URLAccessProfilesListResponse.from_dict(url_access_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


