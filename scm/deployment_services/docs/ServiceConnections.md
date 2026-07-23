# ServiceConnections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_sc** | **str** |  | [optional] 
**id** | **str** | The UUID of the service connection | [readonly] 
**ipsec_tunnel** | **str** |  | 
**name** | **str** | The name of the service connection | 
**nat_pool** | **str** |  | [optional] 
**no_export_community** | **str** |  | [optional] 
**onboarding_type** | **str** |  | [optional] [default to 'classic']
**protocol** | [**ServiceConnectionsProtocol**](ServiceConnectionsProtocol.md) |  | [optional] 
**qos** | [**ServiceConnectionsQos**](ServiceConnectionsQos.md) |  | [optional] 
**region** | **str** |  | 
**region_tag** | **str** |  | [optional] 
**secondary_ipsec_tunnel** | **str** |  | [optional] 
**source_nat** | **bool** |  | [optional] 
**subnets** | **List[str]** |  | [optional] 

## Example

```python
from scm.deployment_services.models.service_connections import ServiceConnections

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnections from a JSON string
service_connections_instance = ServiceConnections.from_json(json)
# print the JSON string representation of the object
print(ServiceConnections.to_json())

# convert the object into a dict
service_connections_dict = service_connections_instance.to_dict()
# create an instance of ServiceConnections from a dict
service_connections_from_dict = ServiceConnections.from_dict(service_connections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


