# ServicesProtocol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tcp** | [**ServicesProtocolTcp**](ServicesProtocolTcp.md) |  | [optional] 
**udp** | [**ServicesProtocolUdp**](ServicesProtocolUdp.md) |  | [optional] 

## Example

```python
from scm.objects.models.services_protocol import ServicesProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesProtocol from a JSON string
services_protocol_instance = ServicesProtocol.from_json(json)
# print the JSON string representation of the object
print(ServicesProtocol.to_json())

# convert the object into a dict
services_protocol_dict = services_protocol_instance.to_dict()
# create an instance of ServicesProtocol from a dict
services_protocol_from_dict = ServicesProtocol.from_dict(services_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


