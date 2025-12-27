# IkeGatewaysProtocolIkev1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dpd** | [**IkeGatewaysProtocolIkev1Dpd**](IkeGatewaysProtocolIkev1Dpd.md) |  | [optional] 
**ike_crypto_profile** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.ike_gateways_protocol_ikev1 import IkeGatewaysProtocolIkev1

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGatewaysProtocolIkev1 from a JSON string
ike_gateways_protocol_ikev1_instance = IkeGatewaysProtocolIkev1.from_json(json)
# print the JSON string representation of the object
print(IkeGatewaysProtocolIkev1.to_json())

# convert the object into a dict
ike_gateways_protocol_ikev1_dict = ike_gateways_protocol_ikev1_instance.to_dict()
# create an instance of IkeGatewaysProtocolIkev1 from a dict
ike_gateways_protocol_ikev1_from_dict = IkeGatewaysProtocolIkev1.from_dict(ike_gateways_protocol_ikev1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


