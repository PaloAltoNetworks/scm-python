# Lldp

LLDP settings for the interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable LLDP on Interface | [default to False]
**high_availability** | [**LldpHighAvailability**](LldpHighAvailability.md) |  | [optional] 
**profile** | **str** | Name of the LLDP profile to assign to the interface | [optional] 

## Example

```python
from scm.network_services.models.lldp import Lldp

# TODO update the JSON string below
json = "{}"
# create an instance of Lldp from a JSON string
lldp_instance = Lldp.from_json(json)
# print the JSON string representation of the object
print(Lldp.to_json())

# convert the object into a dict
lldp_dict = lldp_instance.to_dict()
# create an instance of Lldp from a dict
lldp_from_dict = Lldp.from_dict(lldp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


