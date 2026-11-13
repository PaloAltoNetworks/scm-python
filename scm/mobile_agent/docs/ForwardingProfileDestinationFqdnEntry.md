# ForwardingProfileDestinationFqdnEntry

FQDN entry destination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | alphanumeric string [*0-9a-zA-Z._-] and at most one $ by the end | 
**port** | **int** | Port number for fqdn based destination | [optional] 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_destination_fqdn_entry import ForwardingProfileDestinationFqdnEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileDestinationFqdnEntry from a JSON string
forwarding_profile_destination_fqdn_entry_instance = ForwardingProfileDestinationFqdnEntry.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileDestinationFqdnEntry.to_json())

# convert the object into a dict
forwarding_profile_destination_fqdn_entry_dict = forwarding_profile_destination_fqdn_entry_instance.to_dict()
# create an instance of ForwardingProfileDestinationFqdnEntry from a dict
forwarding_profile_destination_fqdn_entry_from_dict = ForwardingProfileDestinationFqdnEntry.from_dict(forwarding_profile_destination_fqdn_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


