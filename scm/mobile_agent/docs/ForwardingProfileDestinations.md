# ForwardingProfileDestinations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description of the destination | [optional] 
**fqdn** | [**List[ForwardingProfileDestinationFqdnEntry]**](ForwardingProfileDestinationFqdnEntry.md) | List of FQDN based destination entries | [optional] 
**id** | **str** | The UUID of the destination | [optional] [readonly] 
**ip_addresses** | [**List[ForwardingProfileDestinationIpEntry]**](ForwardingProfileDestinationIpEntry.md) | List of IP address based destination entries | [optional] 
**name** | **str** | alphanumeric string [ 0-9a-zA-Z._ -] | 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_destinations import ForwardingProfileDestinations

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileDestinations from a JSON string
forwarding_profile_destinations_instance = ForwardingProfileDestinations.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileDestinations.to_json())

# convert the object into a dict
forwarding_profile_destinations_dict = forwarding_profile_destinations_instance.to_dict()
# create an instance of ForwardingProfileDestinations from a dict
forwarding_profile_destinations_from_dict = ForwardingProfileDestinations.from_dict(forwarding_profile_destinations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


