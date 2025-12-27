# LLDPProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LldpProfiles]**](LldpProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.lldp_profiles_list_response import LLDPProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LLDPProfilesListResponse from a JSON string
lldp_profiles_list_response_instance = LLDPProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(LLDPProfilesListResponse.to_json())

# convert the object into a dict
lldp_profiles_list_response_dict = lldp_profiles_list_response_instance.to_dict()
# create an instance of LLDPProfilesListResponse from a dict
lldp_profiles_list_response_from_dict = LLDPProfilesListResponse.from_dict(lldp_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


