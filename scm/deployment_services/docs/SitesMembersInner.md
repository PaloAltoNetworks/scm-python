# SitesMembersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID of the remote network | [optional] [readonly] 
**mode** | **str** | The mode of the remote network | 
**name** | **str** | The member name | 
**remote_network** | **str** | The remote network name | [optional] 

## Example

```python
from scm.deployment_services.models.sites_members_inner import SitesMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SitesMembersInner from a JSON string
sites_members_inner_instance = SitesMembersInner.from_json(json)
# print the JSON string representation of the object
print(SitesMembersInner.to_json())

# convert the object into a dict
sites_members_inner_dict = sites_members_inner_instance.to_dict()
# create an instance of SitesMembersInner from a dict
sites_members_inner_from_dict = SitesMembersInner.from_dict(sites_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


