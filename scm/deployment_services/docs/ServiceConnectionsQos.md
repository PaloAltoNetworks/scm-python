# ServiceConnectionsQos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**qos_profile** | **str** |  | [optional] 

## Example

```python
from scm.deployment_services.models.service_connections_qos import ServiceConnectionsQos

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnectionsQos from a JSON string
service_connections_qos_instance = ServiceConnectionsQos.from_json(json)
# print the JSON string representation of the object
print(ServiceConnectionsQos.to_json())

# convert the object into a dict
service_connections_qos_dict = service_connections_qos_instance.to_dict()
# create an instance of ServiceConnectionsQos from a dict
service_connections_qos_from_dict = ServiceConnectionsQos.from_dict(service_connections_qos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


