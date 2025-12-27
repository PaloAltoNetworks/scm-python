# IkeGatewaysPeerId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Peer ID string | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.ike_gateways_peer_id import IkeGatewaysPeerId

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGatewaysPeerId from a JSON string
ike_gateways_peer_id_instance = IkeGatewaysPeerId.from_json(json)
# print the JSON string representation of the object
print(IkeGatewaysPeerId.to_json())

# convert the object into a dict
ike_gateways_peer_id_dict = ike_gateways_peer_id_instance.to_dict()
# create an instance of IkeGatewaysPeerId from a dict
ike_gateways_peer_id_from_dict = IkeGatewaysPeerId.from_dict(ike_gateways_peer_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


