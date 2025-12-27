# ServiceRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**route** | [**ServiceRouteRoute**](ServiceRouteRoute.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.device_settings.models.service_route import ServiceRoute

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRoute from a JSON string
service_route_instance = ServiceRoute.from_json(json)
# print the JSON string representation of the object
print(ServiceRoute.to_json())

# convert the object into a dict
service_route_dict = service_route_instance.to_dict()
# create an instance of ServiceRoute from a dict
service_route_from_dict = ServiceRoute.from_dict(service_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


