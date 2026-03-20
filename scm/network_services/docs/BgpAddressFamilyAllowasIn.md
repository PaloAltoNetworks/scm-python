# BgpAddressFamilyAllowasIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occurrence** | **int** | Number of times the firewalls own AS can be in an AS_PATH | [optional] [default to 1]
**origin** | **object** |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_address_family_allowas_in import BgpAddressFamilyAllowasIn

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAddressFamilyAllowasIn from a JSON string
bgp_address_family_allowas_in_instance = BgpAddressFamilyAllowasIn.from_json(json)
# print the JSON string representation of the object
print(BgpAddressFamilyAllowasIn.to_json())

# convert the object into a dict
bgp_address_family_allowas_in_dict = bgp_address_family_allowas_in_instance.to_dict()
# create an instance of BgpAddressFamilyAllowasIn from a dict
bgp_address_family_allowas_in_from_dict = BgpAddressFamilyAllowasIn.from_dict(bgp_address_family_allowas_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


