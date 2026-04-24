# ForwardingProfileRegionalAndCustomProxies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectivity_preference** | [**List[ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner]**](ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner.md) | List of connectivity methods and their enablement status for establishing proxy connections | [optional] 
**description** | **str** | regional and custom proxy configuration description | [optional] 
**fallback_option** | **str** | Behavior when proxy connection fails - &#39;fail-open&#39; allows direct internet access, &#39;fail-safe&#39; blocks traffic until proxy is restored | [optional] 
**id** | **str** | The UUID of the regional and custom proxy | [optional] [readonly] 
**location_preference** | **str** | Strategy for selecting Prisma Access location - &#39;best-available-pa-location&#39; automatically selects optimal location, &#39;specific-pa-location&#39; uses predefined locations | [optional] 
**name** | **str** | alphanumeric string [ 0-9a-zA-Z ._-] | 
**prisma_access_locations** | [**List[ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner]**](ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner.md) | Select Prisma Access location Americas, Europe and Asia-Pacific. | [optional] 
**proxy_1** | [**ForwardingProfileRegionalAndCustomProxiesProxy1**](ForwardingProfileRegionalAndCustomProxiesProxy1.md) |  | [optional] 
**proxy_2** | [**ForwardingProfileRegionalAndCustomProxiesProxy2**](ForwardingProfileRegionalAndCustomProxiesProxy2.md) |  | [optional] 
**type** | **str** | Proxy configuration type - &#39;gp-and-pac&#39; for GlobalProtect and PAC file forwarding, &#39;ztna-agent&#39; for ZTNA agent forwarding | [optional] [default to 'gp-and-pac']

## Example

```python
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies import ForwardingProfileRegionalAndCustomProxies

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileRegionalAndCustomProxies from a JSON string
forwarding_profile_regional_and_custom_proxies_instance = ForwardingProfileRegionalAndCustomProxies.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileRegionalAndCustomProxies.to_json())

# convert the object into a dict
forwarding_profile_regional_and_custom_proxies_dict = forwarding_profile_regional_and_custom_proxies_instance.to_dict()
# create an instance of ForwardingProfileRegionalAndCustomProxies from a dict
forwarding_profile_regional_and_custom_proxies_from_dict = ForwardingProfileRegionalAndCustomProxies.from_dict(forwarding_profile_regional_and_custom_proxies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


