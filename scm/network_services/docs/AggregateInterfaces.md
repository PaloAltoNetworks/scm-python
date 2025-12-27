# AggregateInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Aggregate interface description | [optional] 
**default_value** | **str** | Default interface assignment | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**layer2** | [**AggregateInterfacesLayer2**](AggregateInterfacesLayer2.md) |  | [optional] 
**layer3** | [**AggregateInterfacesLayer3**](AggregateInterfacesLayer3.md) |  | [optional] 
**name** | **str** | Aggregate interface name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.aggregate_interfaces import AggregateInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateInterfaces from a JSON string
aggregate_interfaces_instance = AggregateInterfaces.from_json(json)
# print the JSON string representation of the object
print(AggregateInterfaces.to_json())

# convert the object into a dict
aggregate_interfaces_dict = aggregate_interfaces_instance.to_dict()
# create an instance of AggregateInterfaces from a dict
aggregate_interfaces_from_dict = AggregateInterfaces.from_dict(aggregate_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


