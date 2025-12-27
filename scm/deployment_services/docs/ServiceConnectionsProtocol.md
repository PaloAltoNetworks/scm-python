# ServiceConnectionsProtocol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp** | [**ServiceConnectionsProtocolBgp**](ServiceConnectionsProtocolBgp.md) |  | [optional] 

## Example

```python
from scm.deployment_services.models.service_connections_protocol import ServiceConnectionsProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnectionsProtocol from a JSON string
service_connections_protocol_instance = ServiceConnectionsProtocol.from_json(json)
# print the JSON string representation of the object
print(ServiceConnectionsProtocol.to_json())

# convert the object into a dict
service_connections_protocol_dict = service_connections_protocol_instance.to_dict()
# create an instance of ServiceConnectionsProtocol from a dict
service_connections_protocol_from_dict = ServiceConnectionsProtocol.from_dict(service_connections_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


