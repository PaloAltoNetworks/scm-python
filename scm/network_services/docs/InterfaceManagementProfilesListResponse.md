# InterfaceManagementProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InterfaceManagementProfiles]**](InterfaceManagementProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_network_services.models.interface_management_profiles_list_response import InterfaceManagementProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceManagementProfilesListResponse from a JSON string
interface_management_profiles_list_response_instance = InterfaceManagementProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(InterfaceManagementProfilesListResponse.to_json())

# convert the object into a dict
interface_management_profiles_list_response_dict = interface_management_profiles_list_response_instance.to_dict()
# create an instance of InterfaceManagementProfilesListResponse from a dict
interface_management_profiles_list_response_from_dict = InterfaceManagementProfilesListResponse.from_dict(interface_management_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


