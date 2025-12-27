# IkeGatewaysProtocolCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fragmentation** | [**IkeGatewaysProtocolCommonFragmentation**](IkeGatewaysProtocolCommonFragmentation.md) |  | [optional] 
**nat_traversal** | [**IkeGatewaysProtocolCommonNatTraversal**](IkeGatewaysProtocolCommonNatTraversal.md) |  | [optional] 
**passive_mode** | **bool** |  | [optional] [default to False]

## Example

```python
from scm_network_services.models.ike_gateways_protocol_common import IkeGatewaysProtocolCommon

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGatewaysProtocolCommon from a JSON string
ike_gateways_protocol_common_instance = IkeGatewaysProtocolCommon.from_json(json)
# print the JSON string representation of the object
print(IkeGatewaysProtocolCommon.to_json())

# convert the object into a dict
ike_gateways_protocol_common_dict = ike_gateways_protocol_common_instance.to_dict()
# create an instance of IkeGatewaysProtocolCommon from a dict
ike_gateways_protocol_common_from_dict = IkeGatewaysProtocolCommon.from_dict(ike_gateways_protocol_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


