# PppoeStaticAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | Static IP address | 

## Example

```python
from scm.network_services.models.pppoe_static_address import PppoeStaticAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PppoeStaticAddress from a JSON string
pppoe_static_address_instance = PppoeStaticAddress.from_json(json)
# print the JSON string representation of the object
print(PppoeStaticAddress.to_json())

# convert the object into a dict
pppoe_static_address_dict = pppoe_static_address_instance.to_dict()
# create an instance of PppoeStaticAddress from a dict
pppoe_static_address_from_dict = PppoeStaticAddress.from_dict(pppoe_static_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


