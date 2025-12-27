# BGPAuthenticationProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BgpAuthProfiles]**](BgpAuthProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_network_services.models.bgp_authentication_profiles_list_response import BGPAuthenticationProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BGPAuthenticationProfilesListResponse from a JSON string
bgp_authentication_profiles_list_response_instance = BGPAuthenticationProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(BGPAuthenticationProfilesListResponse.to_json())

# convert the object into a dict
bgp_authentication_profiles_list_response_dict = bgp_authentication_profiles_list_response_instance.to_dict()
# create an instance of BGPAuthenticationProfilesListResponse from a dict
bgp_authentication_profiles_list_response_from_dict = BGPAuthenticationProfilesListResponse.from_dict(bgp_authentication_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


