# Poe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poe_enabled** | **bool** | Enabled PoE? | [optional] [default to False]
**poe_rsvd_pwr** | **int** | PoE reserved power | [optional] [default to 0]

## Example

```python
from scm_network_services.models.poe import Poe

# TODO update the JSON string below
json = "{}"
# create an instance of Poe from a JSON string
poe_instance = Poe.from_json(json)
# print the JSON string representation of the object
print(Poe.to_json())

# convert the object into a dict
poe_dict = poe_instance.to_dict()
# create an instance of Poe from a dict
poe_from_dict = Poe.from_dict(poe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


