# LogicalRouters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** |  | 
**routing_stack** | **str** |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**vrf** | [**List[LogicalRoutersVrfInner]**](LogicalRoutersVrfInner.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers import LogicalRouters

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRouters from a JSON string
logical_routers_instance = LogicalRouters.from_json(json)
# print the JSON string representation of the object
print(LogicalRouters.to_json())

# convert the object into a dict
logical_routers_dict = logical_routers_instance.to_dict()
# create an instance of LogicalRouters from a dict
logical_routers_from_dict = LogicalRouters.from_dict(logical_routers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


