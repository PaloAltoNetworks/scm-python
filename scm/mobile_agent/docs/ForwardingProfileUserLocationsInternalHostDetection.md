# ForwardingProfileUserLocationsInternalHostDetection

Configuration for detecting internal hosts using IP address and FQDN

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | user location fqdn | 
**ip_address** | **str** | user location ip address | 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_user_locations_internal_host_detection import ForwardingProfileUserLocationsInternalHostDetection

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileUserLocationsInternalHostDetection from a JSON string
forwarding_profile_user_locations_internal_host_detection_instance = ForwardingProfileUserLocationsInternalHostDetection.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileUserLocationsInternalHostDetection.to_json())

# convert the object into a dict
forwarding_profile_user_locations_internal_host_detection_dict = forwarding_profile_user_locations_internal_host_detection_instance.to_dict()
# create an instance of ForwardingProfileUserLocationsInternalHostDetection from a dict
forwarding_profile_user_locations_internal_host_detection_from_dict = ForwardingProfileUserLocationsInternalHostDetection.from_dict(forwarding_profile_user_locations_internal_host_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


