# Pppoe

PPPoE configuration for the interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_concentrator** | **str** | Access concentrator | [optional] 
**authentication** | **str** | Authentication protocol | [optional] 
**default_route_metric** | **int** | Metric of the default route created | [optional] [default to 10]
**enable** | **bool** | Enable PPPoE on the interface | [optional] [default to True]
**passive** | [**PppoePassive**](PppoePassive.md) |  | [optional] 
**password** | **str** | Password | 
**service** | **str** | Service | [optional] 
**static_address** | [**PppoeStaticAddress**](PppoeStaticAddress.md) |  | [optional] 
**username** | **str** | Username | 

## Example

```python
from scm.network_services.models.pppoe import Pppoe

# TODO update the JSON string below
json = "{}"
# create an instance of Pppoe from a JSON string
pppoe_instance = Pppoe.from_json(json)
# print the JSON string representation of the object
print(Pppoe.to_json())

# convert the object into a dict
pppoe_dict = pppoe_instance.to_dict()
# create an instance of Pppoe from a dict
pppoe_from_dict = Pppoe.from_dict(pppoe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


