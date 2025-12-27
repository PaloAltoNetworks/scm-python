# ZoneProtectionProfilesL2SecGroupTagProtectionTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable this exclude list for Ethernet SGT protection. | [optional] 
**name** | **str** | Name for the list of Security Group Tags (SGTs). | 
**tag** | **str** | The Layer 2 SGTs in headers of packets that you want to exclude (drop) when the SGT matches this list in the Zone Protection profile applied to a zone (range is 0 to 65,535). | 

## Example

```python
from scm.network_services.models.zone_protection_profiles_l2_sec_group_tag_protection_tags_inner import ZoneProtectionProfilesL2SecGroupTagProtectionTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesL2SecGroupTagProtectionTagsInner from a JSON string
zone_protection_profiles_l2_sec_group_tag_protection_tags_inner_instance = ZoneProtectionProfilesL2SecGroupTagProtectionTagsInner.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesL2SecGroupTagProtectionTagsInner.to_json())

# convert the object into a dict
zone_protection_profiles_l2_sec_group_tag_protection_tags_inner_dict = zone_protection_profiles_l2_sec_group_tag_protection_tags_inner_instance.to_dict()
# create an instance of ZoneProtectionProfilesL2SecGroupTagProtectionTagsInner from a dict
zone_protection_profiles_l2_sec_group_tag_protection_tags_inner_from_dict = ZoneProtectionProfilesL2SecGroupTagProtectionTagsInner.from_dict(zone_protection_profiles_l2_sec_group_tag_protection_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


