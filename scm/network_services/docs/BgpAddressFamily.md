# BgpAddressFamily


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_path** | [**BgpAddressFamilyAddPath**](BgpAddressFamilyAddPath.md) |  | [optional] 
**allowas_in** | [**BgpAddressFamilyAllowasIn**](BgpAddressFamilyAllowasIn.md) |  | [optional] 
**as_override** | **bool** | Override ASNs in outbound updates if AS-Path equals Remote-AS? | [optional] 
**default_originate** | **bool** | Originate default route? | [optional] 
**default_originate_map** | **str** | Default originate route map | [optional] 
**enable** | **bool** | Enable? | [optional] 
**maximum_prefix** | [**BgpAddressFamilyMaximumPrefix**](BgpAddressFamilyMaximumPrefix.md) |  | [optional] 
**next_hop** | [**BgpAddressFamilyNextHop**](BgpAddressFamilyNextHop.md) |  | [optional] 
**orf** | [**BgpAddressFamilyOrf**](BgpAddressFamilyOrf.md) |  | [optional] 
**remove_private_as** | [**BgpAddressFamilyRemovePrivateAS**](BgpAddressFamilyRemovePrivateAS.md) |  | [optional] 
**route_reflector_client** | **bool** | Route reflector client? | [optional] 
**send_community** | [**BgpAddressFamilySendCommunity**](BgpAddressFamilySendCommunity.md) |  | [optional] 
**soft_reconfig_with_stored_info** | **bool** | Soft reconfiguration of peer with stored routes? | [optional] 

## Example

```python
from scm_network_services.models.bgp_address_family import BgpAddressFamily

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAddressFamily from a JSON string
bgp_address_family_instance = BgpAddressFamily.from_json(json)
# print the JSON string representation of the object
print(BgpAddressFamily.to_json())

# convert the object into a dict
bgp_address_family_dict = bgp_address_family_instance.to_dict()
# create an instance of BgpAddressFamily from a dict
bgp_address_family_from_dict = BgpAddressFamily.from_dict(bgp_address_family_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


