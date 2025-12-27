# SDWANTrafficDistributionProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SdwanTrafficDistributionProfiles]**](SdwanTrafficDistributionProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_network_services.models.sdwan_traffic_distribution_profiles_list_response import SDWANTrafficDistributionProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SDWANTrafficDistributionProfilesListResponse from a JSON string
sdwan_traffic_distribution_profiles_list_response_instance = SDWANTrafficDistributionProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(SDWANTrafficDistributionProfilesListResponse.to_json())

# convert the object into a dict
sdwan_traffic_distribution_profiles_list_response_dict = sdwan_traffic_distribution_profiles_list_response_instance.to_dict()
# create an instance of SDWANTrafficDistributionProfilesListResponse from a dict
sdwan_traffic_distribution_profiles_list_response_from_dict = SDWANTrafficDistributionProfilesListResponse.from_dict(sdwan_traffic_distribution_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


