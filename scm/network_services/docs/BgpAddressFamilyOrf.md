# BgpAddressFamilyOrf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orf_prefix_list** | **str** | ORF prefix list | [optional] 

## Example

```python
from scm_network_services.models.bgp_address_family_orf import BgpAddressFamilyOrf

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAddressFamilyOrf from a JSON string
bgp_address_family_orf_instance = BgpAddressFamilyOrf.from_json(json)
# print the JSON string representation of the object
print(BgpAddressFamilyOrf.to_json())

# convert the object into a dict
bgp_address_family_orf_dict = bgp_address_family_orf_instance.to_dict()
# create an instance of BgpAddressFamilyOrf from a dict
bgp_address_family_orf_from_dict = BgpAddressFamilyOrf.from_dict(bgp_address_family_orf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


