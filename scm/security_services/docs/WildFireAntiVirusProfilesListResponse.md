# WildFireAntiVirusProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WildfireAntiVirusProfiles]**](WildfireAntiVirusProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_security_services.models.wild_fire_anti_virus_profiles_list_response import WildFireAntiVirusProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WildFireAntiVirusProfilesListResponse from a JSON string
wild_fire_anti_virus_profiles_list_response_instance = WildFireAntiVirusProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(WildFireAntiVirusProfilesListResponse.to_json())

# convert the object into a dict
wild_fire_anti_virus_profiles_list_response_dict = wild_fire_anti_virus_profiles_list_response_instance.to_dict()
# create an instance of WildFireAntiVirusProfilesListResponse from a dict
wild_fire_anti_virus_profiles_list_response_from_dict = WildFireAntiVirusProfilesListResponse.from_dict(wild_fire_anti_virus_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


