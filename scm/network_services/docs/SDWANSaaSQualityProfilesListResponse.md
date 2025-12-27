# SDWANSaaSQualityProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SdwanSaasQualityProfiles]**](SdwanSaasQualityProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.sdwan_saa_s_quality_profiles_list_response import SDWANSaaSQualityProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SDWANSaaSQualityProfilesListResponse from a JSON string
sdwan_saa_s_quality_profiles_list_response_instance = SDWANSaaSQualityProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(SDWANSaaSQualityProfilesListResponse.to_json())

# convert the object into a dict
sdwan_saa_s_quality_profiles_list_response_dict = sdwan_saa_s_quality_profiles_list_response_instance.to_dict()
# create an instance of SDWANSaaSQualityProfilesListResponse from a dict
sdwan_saa_s_quality_profiles_list_response_from_dict = SDWANSaaSQualityProfilesListResponse.from_dict(sdwan_saa_s_quality_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


