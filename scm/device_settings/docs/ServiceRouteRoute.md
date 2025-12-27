# ServiceRouteRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**List[ServiceRouteRouteDestinationInner]**](ServiceRouteRouteDestinationInner.md) |  | [optional] 
**service** | [**List[ServiceRouteRouteServiceInner]**](ServiceRouteRouteServiceInner.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.service_route_route import ServiceRouteRoute

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRouteRoute from a JSON string
service_route_route_instance = ServiceRouteRoute.from_json(json)
# print the JSON string representation of the object
print(ServiceRouteRoute.to_json())

# convert the object into a dict
service_route_route_dict = service_route_route_instance.to_dict()
# create an instance of ServiceRouteRoute from a dict
service_route_route_from_dict = ServiceRouteRoute.from_dict(service_route_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


