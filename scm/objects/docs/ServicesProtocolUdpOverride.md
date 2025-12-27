# ServicesProtocolUdpOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | udp session timeout value (in second) | [optional] [default to 30]

## Example

```python
from scm_objects.models.services_protocol_udp_override import ServicesProtocolUdpOverride

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesProtocolUdpOverride from a JSON string
services_protocol_udp_override_instance = ServicesProtocolUdpOverride.from_json(json)
# print the JSON string representation of the object
print(ServicesProtocolUdpOverride.to_json())

# convert the object into a dict
services_protocol_udp_override_dict = services_protocol_udp_override_instance.to_dict()
# create an instance of ServicesProtocolUdpOverride from a dict
services_protocol_udp_override_from_dict = ServicesProtocolUdpOverride.from_dict(services_protocol_udp_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


