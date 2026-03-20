# TACACSServerProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TacacsServerProfiles]**](TacacsServerProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.identity_services.models.tacacs_server_profiles_list_response import TACACSServerProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TACACSServerProfilesListResponse from a JSON string
tacacs_server_profiles_list_response_instance = TACACSServerProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(TACACSServerProfilesListResponse.to_json())

# convert the object into a dict
tacacs_server_profiles_list_response_dict = tacacs_server_profiles_list_response_instance.to_dict()
# create an instance of TACACSServerProfilesListResponse from a dict
tacacs_server_profiles_list_response_from_dict = TACACSServerProfilesListResponse.from_dict(tacacs_server_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


