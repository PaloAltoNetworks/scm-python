# ServicesProtocolTcp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override** | [**ServicesProtocolTcpOverride**](ServicesProtocolTcpOverride.md) |  | [optional] 
**port** | **str** |  | 
**source_port** | **str** |  | [optional] 

## Example

```python
from scm.objects.models.services_protocol_tcp import ServicesProtocolTcp

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesProtocolTcp from a JSON string
services_protocol_tcp_instance = ServicesProtocolTcp.from_json(json)
# print the JSON string representation of the object
print(ServicesProtocolTcp.to_json())

# convert the object into a dict
services_protocol_tcp_dict = services_protocol_tcp_instance.to_dict()
# create an instance of ServicesProtocolTcp from a dict
services_protocol_tcp_from_dict = ServicesProtocolTcp.from_dict(services_protocol_tcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


