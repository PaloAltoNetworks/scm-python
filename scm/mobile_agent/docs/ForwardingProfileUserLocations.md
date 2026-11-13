# ForwardingProfileUserLocations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the user location | [optional] 
**id** | **str** | The UUID of the user location | [optional] [readonly] 
**internal_host_detection** | [**ForwardingProfileUserLocationsInternalHostDetection**](ForwardingProfileUserLocationsInternalHostDetection.md) |  | [optional] 
**ip_addresses** | **List[str]** | List of IP addresses that define the user location | [optional] 
**name** | **str** | alphanumeric string [ 0-9a-zA-Z._-] | [optional] 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_user_locations import ForwardingProfileUserLocations

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileUserLocations from a JSON string
forwarding_profile_user_locations_instance = ForwardingProfileUserLocations.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileUserLocations.to_json())

# convert the object into a dict
forwarding_profile_user_locations_dict = forwarding_profile_user_locations_instance.to_dict()
# create an instance of ForwardingProfileUserLocations from a dict
forwarding_profile_user_locations_from_dict = ForwardingProfileUserLocations.from_dict(forwarding_profile_user_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


