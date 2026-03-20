# DosProtectionProfilesFloodTcpSyn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [default to False]
**red** | [**DosProtectionProfilesFloodIcmpRed**](DosProtectionProfilesFloodIcmpRed.md) |  | [optional] 
**syn_cookies** | [**DosProtectionProfilesFloodTcpSynSynCookies**](DosProtectionProfilesFloodTcpSynSynCookies.md) |  | [optional] 

## Example

```python
from scm.security_services.models.dos_protection_profiles_flood_tcp_syn import DosProtectionProfilesFloodTcpSyn

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionProfilesFloodTcpSyn from a JSON string
dos_protection_profiles_flood_tcp_syn_instance = DosProtectionProfilesFloodTcpSyn.from_json(json)
# print the JSON string representation of the object
print(DosProtectionProfilesFloodTcpSyn.to_json())

# convert the object into a dict
dos_protection_profiles_flood_tcp_syn_dict = dos_protection_profiles_flood_tcp_syn_instance.to_dict()
# create an instance of DosProtectionProfilesFloodTcpSyn from a dict
dos_protection_profiles_flood_tcp_syn_from_dict = DosProtectionProfilesFloodTcpSyn.from_dict(dos_protection_profiles_flood_tcp_syn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


