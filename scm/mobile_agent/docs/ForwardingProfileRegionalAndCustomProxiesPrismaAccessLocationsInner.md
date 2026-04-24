# ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | **List[str]** | Add list of locations separated by space, in that region | [optional] 
**name** | **str** | One of the region from &#39;americas&#39;, &#39;europe&#39;, &#39;apac&#39; | 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies_prisma_access_locations_inner import ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner from a JSON string
forwarding_profile_regional_and_custom_proxies_prisma_access_locations_inner_instance = ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner.to_json())

# convert the object into a dict
forwarding_profile_regional_and_custom_proxies_prisma_access_locations_inner_dict = forwarding_profile_regional_and_custom_proxies_prisma_access_locations_inner_instance.to_dict()
# create an instance of ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner from a dict
forwarding_profile_regional_and_custom_proxies_prisma_access_locations_inner_from_dict = ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner.from_dict(forwarding_profile_regional_and_custom_proxies_prisma_access_locations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


