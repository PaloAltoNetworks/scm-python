# AutoVpnPushResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | **str** | Job ID | [optional] 
**message** | **str** | Job message | [optional] 
**success** | **bool** | Push successful? | [optional] 

## Example

```python
from scm_network_services.models.auto_vpn_push_response import AutoVpnPushResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnPushResponse from a JSON string
auto_vpn_push_response_instance = AutoVpnPushResponse.from_json(json)
# print the JSON string representation of the object
print(AutoVpnPushResponse.to_json())

# convert the object into a dict
auto_vpn_push_response_dict = auto_vpn_push_response_instance.to_dict()
# create an instance of AutoVpnPushResponse from a dict
auto_vpn_push_response_from_dict = AutoVpnPushResponse.from_dict(auto_vpn_push_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


