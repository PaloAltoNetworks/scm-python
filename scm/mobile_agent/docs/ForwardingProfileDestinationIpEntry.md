# ForwardingProfileDestinationIpEntry

IP address entry destination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | IP address with wildcards and CIDR notation support | 
**port** | **int** | Port number for IP address based destination | [optional] 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_destination_ip_entry import ForwardingProfileDestinationIpEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileDestinationIpEntry from a JSON string
forwarding_profile_destination_ip_entry_instance = ForwardingProfileDestinationIpEntry.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileDestinationIpEntry.to_json())

# convert the object into a dict
forwarding_profile_destination_ip_entry_dict = forwarding_profile_destination_ip_entry_instance.to_dict()
# create an instance of ForwardingProfileDestinationIpEntry from a dict
forwarding_profile_destination_ip_entry_from_dict = ForwardingProfileDestinationIpEntry.from_dict(forwarding_profile_destination_ip_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


