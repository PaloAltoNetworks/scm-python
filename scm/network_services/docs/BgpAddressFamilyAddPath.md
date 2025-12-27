# BgpAddressFamilyAddPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_all_paths** | **bool** | Advertise all paths to peer? | [optional] 
**tx_bestpath_per_as** | **bool** | Advertise the bestpath per each neighboring AS? | [optional] 

## Example

```python
from scm_network_services.models.bgp_address_family_add_path import BgpAddressFamilyAddPath

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAddressFamilyAddPath from a JSON string
bgp_address_family_add_path_instance = BgpAddressFamilyAddPath.from_json(json)
# print the JSON string representation of the object
print(BgpAddressFamilyAddPath.to_json())

# convert the object into a dict
bgp_address_family_add_path_dict = bgp_address_family_add_path_instance.to_dict()
# create an instance of BgpAddressFamilyAddPath from a dict
bgp_address_family_add_path_from_dict = BgpAddressFamilyAddPath.from_dict(bgp_address_family_add_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


