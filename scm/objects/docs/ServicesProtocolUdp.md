# ServicesProtocolUdp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override** | [**ServicesProtocolUdpOverride**](ServicesProtocolUdpOverride.md) |  | [optional] 
**port** | **str** |  | 
**source_port** | **str** |  | [optional] 

## Example

```python
from scm.objects.models.services_protocol_udp import ServicesProtocolUdp

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesProtocolUdp from a JSON string
services_protocol_udp_instance = ServicesProtocolUdp.from_json(json)
# print the JSON string representation of the object
print(ServicesProtocolUdp.to_json())

# convert the object into a dict
services_protocol_udp_dict = services_protocol_udp_instance.to_dict()
# create an instance of ServicesProtocolUdp from a dict
services_protocol_udp_from_dict = ServicesProtocolUdp.from_dict(services_protocol_udp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


