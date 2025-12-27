# LdapServerProfilesServerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The LDAP server IP address | [optional] 
**name** | **str** | The LDAP server name | [optional] 
**port** | **int** | The LDAP server port | [optional] 

## Example

```python
from scm_identity_services.models.ldap_server_profiles_server_inner import LdapServerProfilesServerInner

# TODO update the JSON string below
json = "{}"
# create an instance of LdapServerProfilesServerInner from a JSON string
ldap_server_profiles_server_inner_instance = LdapServerProfilesServerInner.from_json(json)
# print the JSON string representation of the object
print(LdapServerProfilesServerInner.to_json())

# convert the object into a dict
ldap_server_profiles_server_inner_dict = ldap_server_profiles_server_inner_instance.to_dict()
# create an instance of LdapServerProfilesServerInner from a dict
ldap_server_profiles_server_inner_from_dict = LdapServerProfilesServerInner.from_dict(ldap_server_profiles_server_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


