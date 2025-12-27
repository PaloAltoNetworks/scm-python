# IkeGatewaysProtocol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ikev1** | [**IkeGatewaysProtocolIkev1**](IkeGatewaysProtocolIkev1.md) |  | [optional] 
**ikev2** | [**IkeGatewaysProtocolIkev1**](IkeGatewaysProtocolIkev1.md) |  | [optional] 
**version** | **str** |  | [optional] [default to 'ikev2-preferred']

## Example

```python
from scm_network_services.models.ike_gateways_protocol import IkeGatewaysProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGatewaysProtocol from a JSON string
ike_gateways_protocol_instance = IkeGatewaysProtocol.from_json(json)
# print the JSON string representation of the object
print(IkeGatewaysProtocol.to_json())

# convert the object into a dict
ike_gateways_protocol_dict = ike_gateways_protocol_instance.to_dict()
# create an instance of IkeGatewaysProtocol from a dict
ike_gateways_protocol_from_dict = IkeGatewaysProtocol.from_dict(ike_gateways_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


