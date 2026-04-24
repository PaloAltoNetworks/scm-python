# ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether this connectivity method is enabled for use in the proxy configuration | [optional] [default to False]
**name** | **str** | Connectivity method type - &#39;tunnel&#39; for VPN tunnels, &#39;proxy&#39; for HTTP/HTTPS proxies, &#39;adns&#39; for authenticated DNS, &#39;masque&#39; for MASQUE protocol | 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies_connectivity_preference_inner import ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner from a JSON string
forwarding_profile_regional_and_custom_proxies_connectivity_preference_inner_instance = ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner.to_json())

# convert the object into a dict
forwarding_profile_regional_and_custom_proxies_connectivity_preference_inner_dict = forwarding_profile_regional_and_custom_proxies_connectivity_preference_inner_instance.to_dict()
# create an instance of ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner from a dict
forwarding_profile_regional_and_custom_proxies_connectivity_preference_inner_from_dict = ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner.from_dict(forwarding_profile_regional_and_custom_proxies_connectivity_preference_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


