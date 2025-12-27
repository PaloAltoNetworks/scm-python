# ServiceConnectionsProtocolBgp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**do_not_export_routes** | **bool** |  | [optional] 
**enable** | **bool** |  | [optional] 
**fast_failover** | **bool** |  | [optional] 
**local_ip_address** | **str** |  | [optional] 
**originate_default_route** | **bool** |  | [optional] 
**peer_as** | **str** |  | [optional] 
**peer_ip_address** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**summarize_mobile_user_routes** | **bool** |  | [optional] 

## Example

```python
from scm.deployment_services.models.service_connections_protocol_bgp import ServiceConnectionsProtocolBgp

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnectionsProtocolBgp from a JSON string
service_connections_protocol_bgp_instance = ServiceConnectionsProtocolBgp.from_json(json)
# print the JSON string representation of the object
print(ServiceConnectionsProtocolBgp.to_json())

# convert the object into a dict
service_connections_protocol_bgp_dict = service_connections_protocol_bgp_instance.to_dict()
# create an instance of ServiceConnectionsProtocolBgp from a dict
service_connections_protocol_bgp_from_dict = ServiceConnectionsProtocolBgp.from_dict(service_connections_protocol_bgp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


