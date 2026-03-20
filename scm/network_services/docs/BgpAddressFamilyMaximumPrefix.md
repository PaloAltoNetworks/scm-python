# BgpAddressFamilyMaximumPrefix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**BgpAddressFamilyMaximumPrefixAction**](BgpAddressFamilyMaximumPrefixAction.md) |  | [optional] 
**num_prefixes** | **int** | Maximum number of prefixes | [optional] 
**threshold** | **int** | Threshold percentage of the maximum number of prefixes | [optional] 

## Example

```python
from scm.network_services.models.bgp_address_family_maximum_prefix import BgpAddressFamilyMaximumPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAddressFamilyMaximumPrefix from a JSON string
bgp_address_family_maximum_prefix_instance = BgpAddressFamilyMaximumPrefix.from_json(json)
# print the JSON string representation of the object
print(BgpAddressFamilyMaximumPrefix.to_json())

# convert the object into a dict
bgp_address_family_maximum_prefix_dict = bgp_address_family_maximum_prefix_instance.to_dict()
# create an instance of BgpAddressFamilyMaximumPrefix from a dict
bgp_address_family_maximum_prefix_from_dict = BgpAddressFamilyMaximumPrefix.from_dict(bgp_address_family_maximum_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


