# DosProtectionProfilesFloodTcpSynSynCookies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_rate** | **int** | Connection rate (cps) to activate SYN cookies proxy | [default to 0]
**alarm_rate** | **int** | Connection rate (cps) to generate alarm | [default to 10000]
**block** | [**DosProtectionProfilesFloodTcpSynSynCookiesBlock**](DosProtectionProfilesFloodTcpSynSynCookiesBlock.md) |  | [optional] 
**maximal_rate** | **int** | Maximum connection rate (cps) allowed | [default to 1000000]

## Example

```python
from scm.security_services.models.dos_protection_profiles_flood_tcp_syn_syn_cookies import DosProtectionProfilesFloodTcpSynSynCookies

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionProfilesFloodTcpSynSynCookies from a JSON string
dos_protection_profiles_flood_tcp_syn_syn_cookies_instance = DosProtectionProfilesFloodTcpSynSynCookies.from_json(json)
# print the JSON string representation of the object
print(DosProtectionProfilesFloodTcpSynSynCookies.to_json())

# convert the object into a dict
dos_protection_profiles_flood_tcp_syn_syn_cookies_dict = dos_protection_profiles_flood_tcp_syn_syn_cookies_instance.to_dict()
# create an instance of DosProtectionProfilesFloodTcpSynSynCookies from a dict
dos_protection_profiles_flood_tcp_syn_syn_cookies_from_dict = DosProtectionProfilesFloodTcpSynSynCookies.from_dict(dos_protection_profiles_flood_tcp_syn_syn_cookies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


