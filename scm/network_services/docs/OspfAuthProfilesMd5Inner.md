# OspfAuthProfilesMd5Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | MD5 hash | [optional] 
**name** | **int** | Key ID | [optional] 
**preferred** | **bool** | Preferred? | [optional] 

## Example

```python
from scm.network_services.models.ospf_auth_profiles_md5_inner import OspfAuthProfilesMd5Inner

# TODO update the JSON string below
json = "{}"
# create an instance of OspfAuthProfilesMd5Inner from a JSON string
ospf_auth_profiles_md5_inner_instance = OspfAuthProfilesMd5Inner.from_json(json)
# print the JSON string representation of the object
print(OspfAuthProfilesMd5Inner.to_json())

# convert the object into a dict
ospf_auth_profiles_md5_inner_dict = ospf_auth_profiles_md5_inner_instance.to_dict()
# create an instance of OspfAuthProfilesMd5Inner from a dict
ospf_auth_profiles_md5_inner_from_dict = OspfAuthProfilesMd5Inner.from_dict(ospf_auth_profiles_md5_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


