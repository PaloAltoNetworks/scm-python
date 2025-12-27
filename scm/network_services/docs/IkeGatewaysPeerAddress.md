# IkeGatewaysPeerAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic** | **object** |  | [optional] 
**fqdn** | **str** | peer gateway FQDN name | [optional] 
**ip** | **str** | peer gateway has static IP address | [optional] 

## Example

```python
from scm_network_services.models.ike_gateways_peer_address import IkeGatewaysPeerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGatewaysPeerAddress from a JSON string
ike_gateways_peer_address_instance = IkeGatewaysPeerAddress.from_json(json)
# print the JSON string representation of the object
print(IkeGatewaysPeerAddress.to_json())

# convert the object into a dict
ike_gateways_peer_address_dict = ike_gateways_peer_address_instance.to_dict()
# create an instance of IkeGatewaysPeerAddress from a dict
ike_gateways_peer_address_from_dict = IkeGatewaysPeerAddress.from_dict(ike_gateways_peer_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


