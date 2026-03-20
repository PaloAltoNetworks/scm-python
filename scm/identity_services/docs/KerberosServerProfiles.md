# KerberosServerProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the Kerberos server profile | [readonly] 
**name** | **str** | The name of the Kerberos server profile | 
**server** | [**List[KerberosServerProfilesServerInner]**](KerberosServerProfilesServerInner.md) | The Kerberos server configuration | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.identity_services.models.kerberos_server_profiles import KerberosServerProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosServerProfiles from a JSON string
kerberos_server_profiles_instance = KerberosServerProfiles.from_json(json)
# print the JSON string representation of the object
print(KerberosServerProfiles.to_json())

# convert the object into a dict
kerberos_server_profiles_dict = kerberos_server_profiles_instance.to_dict()
# create an instance of KerberosServerProfiles from a dict
kerberos_server_profiles_from_dict = KerberosServerProfiles.from_dict(kerberos_server_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


