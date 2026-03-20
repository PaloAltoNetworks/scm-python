# ServiceRouteRouteDestinationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**source** | [**ServiceRouteRouteDestinationInnerSource**](ServiceRouteRouteDestinationInnerSource.md) |  | [optional] 

## Example

```python
from scm.device_settings.models.service_route_route_destination_inner import ServiceRouteRouteDestinationInner

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRouteRouteDestinationInner from a JSON string
service_route_route_destination_inner_instance = ServiceRouteRouteDestinationInner.from_json(json)
# print the JSON string representation of the object
print(ServiceRouteRouteDestinationInner.to_json())

# convert the object into a dict
service_route_route_destination_inner_dict = service_route_route_destination_inner_instance.to_dict()
# create an instance of ServiceRouteRouteDestinationInner from a dict
service_route_route_destination_inner_from_dict = ServiceRouteRouteDestinationInner.from_dict(service_route_route_destination_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


