# ForwardingProfileRegionalAndCustomProxiesProxy2

secondary regional and custom proxy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Fqdn of the secondary (backup) proxy server used for failover scenarios | [optional] 
**location** | **str** | Geographic or network location identifier for the secondary proxy server | [optional] 
**port** | **int** | port number for secondary proxy | [optional] 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies_proxy2 import ForwardingProfileRegionalAndCustomProxiesProxy2

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileRegionalAndCustomProxiesProxy2 from a JSON string
forwarding_profile_regional_and_custom_proxies_proxy2_instance = ForwardingProfileRegionalAndCustomProxiesProxy2.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileRegionalAndCustomProxiesProxy2.to_json())

# convert the object into a dict
forwarding_profile_regional_and_custom_proxies_proxy2_dict = forwarding_profile_regional_and_custom_proxies_proxy2_instance.to_dict()
# create an instance of ForwardingProfileRegionalAndCustomProxiesProxy2 from a dict
forwarding_profile_regional_and_custom_proxies_proxy2_from_dict = ForwardingProfileRegionalAndCustomProxiesProxy2.from_dict(forwarding_profile_regional_and_custom_proxies_proxy2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


