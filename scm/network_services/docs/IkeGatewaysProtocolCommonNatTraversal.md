# IkeGatewaysProtocolCommonNatTraversal

Enables NAT traversal for the IKE gateway.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] [default to True]

## Example

```python
from scm.network_services.models.ike_gateways_protocol_common_nat_traversal import IkeGatewaysProtocolCommonNatTraversal

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGatewaysProtocolCommonNatTraversal from a JSON string
ike_gateways_protocol_common_nat_traversal_instance = IkeGatewaysProtocolCommonNatTraversal.from_json(json)
# print the JSON string representation of the object
print(IkeGatewaysProtocolCommonNatTraversal.to_json())

# convert the object into a dict
ike_gateways_protocol_common_nat_traversal_dict = ike_gateways_protocol_common_nat_traversal_instance.to_dict()
# create an instance of IkeGatewaysProtocolCommonNatTraversal from a dict
ike_gateways_protocol_common_nat_traversal_from_dict = IkeGatewaysProtocolCommonNatTraversal.from_dict(ike_gateways_protocol_common_nat_traversal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


