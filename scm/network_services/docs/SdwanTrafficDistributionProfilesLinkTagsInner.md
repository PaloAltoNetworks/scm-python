# SdwanTrafficDistributionProfilesLinkTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Link-Tag used for identifying a set of interfaces | 
**weight** | **int** | Weight (percentage) (only used when &#x60;traffic-distribution&#x60; is &#x60;Weighted Session Distribution&#x60;) | [optional] 

## Example

```python
from scm.network_services.models.sdwan_traffic_distribution_profiles_link_tags_inner import SdwanTrafficDistributionProfilesLinkTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanTrafficDistributionProfilesLinkTagsInner from a JSON string
sdwan_traffic_distribution_profiles_link_tags_inner_instance = SdwanTrafficDistributionProfilesLinkTagsInner.from_json(json)
# print the JSON string representation of the object
print(SdwanTrafficDistributionProfilesLinkTagsInner.to_json())

# convert the object into a dict
sdwan_traffic_distribution_profiles_link_tags_inner_dict = sdwan_traffic_distribution_profiles_link_tags_inner_instance.to_dict()
# create an instance of SdwanTrafficDistributionProfilesLinkTagsInner from a dict
sdwan_traffic_distribution_profiles_link_tags_inner_from_dict = SdwanTrafficDistributionProfilesLinkTagsInner.from_dict(sdwan_traffic_distribution_profiles_link_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


