# ForwardingProfileRegionalAndCustomProxiesProxy1

primary regional and custom proxy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | fqdn of the primary proxy server (supports wildcards and alphanumeric characters with dots, hyphens, and underscores) | [optional] 
**location** | **str** | Geographic or network location identifier for the primary proxy server | [optional] 
**port** | **int** | port number for primary proxy | [optional] 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies_proxy1 import ForwardingProfileRegionalAndCustomProxiesProxy1

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileRegionalAndCustomProxiesProxy1 from a JSON string
forwarding_profile_regional_and_custom_proxies_proxy1_instance = ForwardingProfileRegionalAndCustomProxiesProxy1.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileRegionalAndCustomProxiesProxy1.to_json())

# convert the object into a dict
forwarding_profile_regional_and_custom_proxies_proxy1_dict = forwarding_profile_regional_and_custom_proxies_proxy1_instance.to_dict()
# create an instance of ForwardingProfileRegionalAndCustomProxiesProxy1 from a dict
forwarding_profile_regional_and_custom_proxies_proxy1_from_dict = ForwardingProfileRegionalAndCustomProxiesProxy1.from_dict(forwarding_profile_regional_and_custom_proxies_proxy1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


