# ServicesProtocolTcpOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**halfclose_timeout** | **int** | tcp session half-close timeout value (in second) | [optional] [default to 120]
**timeout** | **int** | tcp session timeout value (in second) | [optional] [default to 3600]
**timewait_timeout** | **int** | tcp session time-wait timeout value (in second) | [optional] [default to 15]

## Example

```python
from scm_objects.models.services_protocol_tcp_override import ServicesProtocolTcpOverride

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesProtocolTcpOverride from a JSON string
services_protocol_tcp_override_instance = ServicesProtocolTcpOverride.from_json(json)
# print the JSON string representation of the object
print(ServicesProtocolTcpOverride.to_json())

# convert the object into a dict
services_protocol_tcp_override_dict = services_protocol_tcp_override_instance.to_dict()
# create an instance of ServicesProtocolTcpOverride from a dict
services_protocol_tcp_override_from_dict = ServicesProtocolTcpOverride.from_dict(services_protocol_tcp_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


