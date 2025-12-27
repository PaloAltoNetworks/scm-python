# IkeGateways


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**IkeGatewaysAuthentication**](IkeGatewaysAuthentication.md) |  | 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**local_address** | [**IkeGatewaysLocalAddress**](IkeGatewaysLocalAddress.md) |  | [optional] 
**local_id** | [**IkeGatewaysLocalId**](IkeGatewaysLocalId.md) |  | [optional] 
**name** | **str** | Alphanumeric string begin with letter: [0-9a-zA-Z._-] | 
**peer_address** | [**IkeGatewaysPeerAddress**](IkeGatewaysPeerAddress.md) |  | 
**peer_id** | [**IkeGatewaysPeerId**](IkeGatewaysPeerId.md) |  | [optional] 
**protocol** | [**IkeGatewaysProtocol**](IkeGatewaysProtocol.md) |  | 
**protocol_common** | [**IkeGatewaysProtocolCommon**](IkeGatewaysProtocolCommon.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.ike_gateways import IkeGateways

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGateways from a JSON string
ike_gateways_instance = IkeGateways.from_json(json)
# print the JSON string representation of the object
print(IkeGateways.to_json())

# convert the object into a dict
ike_gateways_dict = ike_gateways_instance.to_dict()
# create an instance of IkeGateways from a dict
ike_gateways_from_dict = IkeGateways.from_dict(ike_gateways_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


