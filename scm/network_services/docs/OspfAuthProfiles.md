# OspfAuthProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**md5** | [**List[OspfAuthProfilesMd5Inner]**](OspfAuthProfilesMd5Inner.md) | MD5s | [optional] 
**name** | **str** | Profile name | 
**password** | **str** | Password | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.ospf_auth_profiles import OspfAuthProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of OspfAuthProfiles from a JSON string
ospf_auth_profiles_instance = OspfAuthProfiles.from_json(json)
# print the JSON string representation of the object
print(OspfAuthProfiles.to_json())

# convert the object into a dict
ospf_auth_profiles_dict = ospf_auth_profiles_instance.to_dict()
# create an instance of OspfAuthProfiles from a dict
ospf_auth_profiles_from_dict = OspfAuthProfiles.from_dict(ospf_auth_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


