# AggregateInterfacesLayer2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lacp** | [**Lacp**](Lacp.md) |  | [optional] 
**netflow_profile** | **str** | Name of Netflow Profile to assign to Interface | [optional] 
**vlan_tag** | **str** | VLAN tag | [optional] 

## Example

```python
from scm.network_services.models.aggregate_interfaces_layer2 import AggregateInterfacesLayer2

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateInterfacesLayer2 from a JSON string
aggregate_interfaces_layer2_instance = AggregateInterfacesLayer2.from_json(json)
# print the JSON string representation of the object
print(AggregateInterfacesLayer2.to_json())

# convert the object into a dict
aggregate_interfaces_layer2_dict = aggregate_interfaces_layer2_instance.to_dict()
# create an instance of AggregateInterfacesLayer2 from a dict
aggregate_interfaces_layer2_from_dict = AggregateInterfacesLayer2.from_dict(aggregate_interfaces_layer2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


