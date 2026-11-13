# GlobalProtectDestinationsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ForwardingProfileDestinations]**](ForwardingProfileDestinations.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.mobile_agent.models.global_protect_destinations_list_response import GlobalProtectDestinationsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalProtectDestinationsListResponse from a JSON string
global_protect_destinations_list_response_instance = GlobalProtectDestinationsListResponse.from_json(json)
# print the JSON string representation of the object
print(GlobalProtectDestinationsListResponse.to_json())

# convert the object into a dict
global_protect_destinations_list_response_dict = global_protect_destinations_list_response_instance.to_dict()
# create an instance of GlobalProtectDestinationsListResponse from a dict
global_protect_destinations_list_response_from_dict = GlobalProtectDestinationsListResponse.from_dict(global_protect_destinations_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


