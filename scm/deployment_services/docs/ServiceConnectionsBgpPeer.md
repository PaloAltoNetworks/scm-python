# ServiceConnectionsBgpPeer

Secondary BGP peer (secondary WAN)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_ip_address** | **str** | Local peer IP address (secondary WAN) | [optional] 
**local_ipv6_address** | **str** | Local peer IPv6 address (secondary WAN) | [optional] 
**peer_ip_address** | **str** | Remote peer IP address (secondary WAN) | [optional] 
**peer_ipv6_address** | **str** | Remote peer IPv6 address (secondary WAN) | [optional] 
**secret** | **str** | BGP peering secret (secondary WAN) | [optional] 

## Example

```python
from scm.deployment_services.models.service_connections_bgp_peer import ServiceConnectionsBgpPeer

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnectionsBgpPeer from a JSON string
service_connections_bgp_peer_instance = ServiceConnectionsBgpPeer.from_json(json)
# print the JSON string representation of the object
print(ServiceConnectionsBgpPeer.to_json())

# convert the object into a dict
service_connections_bgp_peer_dict = service_connections_bgp_peer_instance.to_dict()
# create an instance of ServiceConnectionsBgpPeer from a dict
service_connections_bgp_peer_from_dict = ServiceConnectionsBgpPeer.from_dict(service_connections_bgp_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


