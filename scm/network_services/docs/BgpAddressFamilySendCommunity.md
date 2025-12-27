# BgpAddressFamilySendCommunity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **object** |  | [optional] 
**both** | **object** |  | [optional] 
**extended** | **object** |  | [optional] 
**large** | **object** |  | [optional] 
**standard** | **object** |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_address_family_send_community import BgpAddressFamilySendCommunity

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAddressFamilySendCommunity from a JSON string
bgp_address_family_send_community_instance = BgpAddressFamilySendCommunity.from_json(json)
# print the JSON string representation of the object
print(BgpAddressFamilySendCommunity.to_json())

# convert the object into a dict
bgp_address_family_send_community_dict = bgp_address_family_send_community_instance.to_dict()
# create an instance of BgpAddressFamilySendCommunity from a dict
bgp_address_family_send_community_from_dict = BgpAddressFamilySendCommunity.from_dict(bgp_address_family_send_community_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


