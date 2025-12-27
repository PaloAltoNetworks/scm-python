# KerberosServerProfilesServerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The Kerberos server IP address | [optional] 
**name** | **str** | The Kerberos server name | [optional] 
**port** | **int** | The Kerberos server port | [optional] 

## Example

```python
from scm.identity_services.models.kerberos_server_profiles_server_inner import KerberosServerProfilesServerInner

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosServerProfilesServerInner from a JSON string
kerberos_server_profiles_server_inner_instance = KerberosServerProfilesServerInner.from_json(json)
# print the JSON string representation of the object
print(KerberosServerProfilesServerInner.to_json())

# convert the object into a dict
kerberos_server_profiles_server_inner_dict = kerberos_server_profiles_server_inner_instance.to_dict()
# create an instance of KerberosServerProfilesServerInner from a dict
kerberos_server_profiles_server_inner_from_dict = KerberosServerProfilesServerInner.from_dict(kerberos_server_profiles_server_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


