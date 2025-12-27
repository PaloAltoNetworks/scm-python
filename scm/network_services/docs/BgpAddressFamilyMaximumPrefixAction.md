# BgpAddressFamilyMaximumPrefixAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restart** | [**BgpAddressFamilyMaximumPrefixActionRestart**](BgpAddressFamilyMaximumPrefixActionRestart.md) |  | [optional] 
**warning_only** | **object** |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_address_family_maximum_prefix_action import BgpAddressFamilyMaximumPrefixAction

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAddressFamilyMaximumPrefixAction from a JSON string
bgp_address_family_maximum_prefix_action_instance = BgpAddressFamilyMaximumPrefixAction.from_json(json)
# print the JSON string representation of the object
print(BgpAddressFamilyMaximumPrefixAction.to_json())

# convert the object into a dict
bgp_address_family_maximum_prefix_action_dict = bgp_address_family_maximum_prefix_action_instance.to_dict()
# create an instance of BgpAddressFamilyMaximumPrefixAction from a dict
bgp_address_family_maximum_prefix_action_from_dict = BgpAddressFamilyMaximumPrefixAction.from_dict(bgp_address_family_maximum_prefix_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


