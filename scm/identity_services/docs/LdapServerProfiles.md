# LdapServerProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | The base DN | [optional] 
**bind_dn** | **str** | The bind DN | [optional] 
**bind_password** | **str** | The bind password | [optional] 
**bind_timelimit** | **str** | The bind timeout (seconds) | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the LDAP server profile | [readonly] 
**ldap_type** | **str** | The LDAP server time | [optional] 
**name** | **str** | The name of the LDAP server profile | 
**retry_interval** | **int** | The search retry interval (seconds) | [optional] 
**server** | [**List[LdapServerProfilesServerInner]**](LdapServerProfilesServerInner.md) | The LDAP server configuration | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**ssl** | **bool** | Require SSL/TLS secured connection? | [optional] 
**timelimit** | **int** | The search timeout (seconds) | [optional] 
**verify_server_certificate** | **bool** | Verify server certificate for SSL sessions? | [optional] 

## Example

```python
from scm_identity_services.models.ldap_server_profiles import LdapServerProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of LdapServerProfiles from a JSON string
ldap_server_profiles_instance = LdapServerProfiles.from_json(json)
# print the JSON string representation of the object
print(LdapServerProfiles.to_json())

# convert the object into a dict
ldap_server_profiles_dict = ldap_server_profiles_instance.to_dict()
# create an instance of LdapServerProfiles from a dict
ldap_server_profiles_from_dict = LdapServerProfiles.from_dict(ldap_server_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


