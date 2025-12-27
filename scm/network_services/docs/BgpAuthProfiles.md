# BgpAuthProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Profile name | 
**secret** | **str** | BGP authentication key | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.bgp_auth_profiles import BgpAuthProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAuthProfiles from a JSON string
bgp_auth_profiles_instance = BgpAuthProfiles.from_json(json)
# print the JSON string representation of the object
print(BgpAuthProfiles.to_json())

# convert the object into a dict
bgp_auth_profiles_dict = bgp_auth_profiles_instance.to_dict()
# create an instance of BgpAuthProfiles from a dict
bgp_auth_profiles_from_dict = BgpAuthProfiles.from_dict(bgp_auth_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


