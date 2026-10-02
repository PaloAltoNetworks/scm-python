# ForwardingProfileGlobalProtectProxyGlobalProtectProxy

Global Protect proxy-based forwarding configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_rule** | [**BlockRuleBasic**](BlockRuleBasic.md) |  | [optional] 
**forwarding_rules** | [**List[ForwardingRuleBasic]**](ForwardingRuleBasic.md) | List of GlobalProtect proxy-based forwarding rules | [optional] 
**pac_upload** | **bool** | User uploaded PAC file for Global Protect proxy-based forwarding configuration | [optional] [default to False]

## Example

```python
from scm.mobile_agent.models.forwarding_profile_global_protect_proxy_global_protect_proxy import ForwardingProfileGlobalProtectProxyGlobalProtectProxy

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileGlobalProtectProxyGlobalProtectProxy from a JSON string
forwarding_profile_global_protect_proxy_global_protect_proxy_instance = ForwardingProfileGlobalProtectProxyGlobalProtectProxy.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileGlobalProtectProxyGlobalProtectProxy.to_json())

# convert the object into a dict
forwarding_profile_global_protect_proxy_global_protect_proxy_dict = forwarding_profile_global_protect_proxy_global_protect_proxy_instance.to_dict()
# create an instance of ForwardingProfileGlobalProtectProxyGlobalProtectProxy from a dict
forwarding_profile_global_protect_proxy_global_protect_proxy_from_dict = ForwardingProfileGlobalProtectProxyGlobalProtectProxy.from_dict(forwarding_profile_global_protect_proxy_global_protect_proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


