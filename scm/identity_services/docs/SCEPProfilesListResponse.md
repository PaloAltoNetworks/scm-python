# SCEPProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ScepProfiles]**](ScepProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.identity_services.models.scep_profiles_list_response import SCEPProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SCEPProfilesListResponse from a JSON string
scep_profiles_list_response_instance = SCEPProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(SCEPProfilesListResponse.to_json())

# convert the object into a dict
scep_profiles_list_response_dict = scep_profiles_list_response_instance.to_dict()
# create an instance of SCEPProfilesListResponse from a dict
scep_profiles_list_response_from_dict = SCEPProfilesListResponse.from_dict(scep_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


