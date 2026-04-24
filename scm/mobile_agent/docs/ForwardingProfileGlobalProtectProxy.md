# ForwardingProfileGlobalProtectProxy

GlobalProtect proxy-based forwarding profile configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_protect_proxy** | [**ForwardingProfileGlobalProtectProxyGlobalProtectProxy**](ForwardingProfileGlobalProtectProxyGlobalProtectProxy.md) |  | [optional] 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_global_protect_proxy import ForwardingProfileGlobalProtectProxy

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileGlobalProtectProxy from a JSON string
forwarding_profile_global_protect_proxy_instance = ForwardingProfileGlobalProtectProxy.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileGlobalProtectProxy.to_json())

# convert the object into a dict
forwarding_profile_global_protect_proxy_dict = forwarding_profile_global_protect_proxy_instance.to_dict()
# create an instance of ForwardingProfileGlobalProtectProxy from a dict
forwarding_profile_global_protect_proxy_from_dict = ForwardingProfileGlobalProtectProxy.from_dict(forwarding_profile_global_protect_proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


