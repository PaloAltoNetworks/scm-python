# PppoePassive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Passive Mode enabled | [default to False]

## Example

```python
from scm.network_services.models.pppoe_passive import PppoePassive

# TODO update the JSON string below
json = "{}"
# create an instance of PppoePassive from a JSON string
pppoe_passive_instance = PppoePassive.from_json(json)
# print the JSON string representation of the object
print(PppoePassive.to_json())

# convert the object into a dict
pppoe_passive_dict = pppoe_passive_instance.to_dict()
# create an instance of PppoePassive from a dict
pppoe_passive_from_dict = PppoePassive.from_dict(pppoe_passive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


