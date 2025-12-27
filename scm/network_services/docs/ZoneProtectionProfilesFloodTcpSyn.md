# ZoneProtectionProfilesFloodTcpSyn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable protection against SYN floods? | [optional] 
**red** | [**ZoneProtectionProfilesFloodTcpSynRed**](ZoneProtectionProfilesFloodTcpSynRed.md) |  | [optional] 
**syn_cookies** | [**ZoneProtectionProfilesFloodTcpSynSynCookies**](ZoneProtectionProfilesFloodTcpSynSynCookies.md) |  | [optional] 

## Example

```python
from scm.network_services.models.zone_protection_profiles_flood_tcp_syn import ZoneProtectionProfilesFloodTcpSyn

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodTcpSyn from a JSON string
zone_protection_profiles_flood_tcp_syn_instance = ZoneProtectionProfilesFloodTcpSyn.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodTcpSyn.to_json())

# convert the object into a dict
zone_protection_profiles_flood_tcp_syn_dict = zone_protection_profiles_flood_tcp_syn_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodTcpSyn from a dict
zone_protection_profiles_flood_tcp_syn_from_dict = ZoneProtectionProfilesFloodTcpSyn.from_dict(zone_protection_profiles_flood_tcp_syn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


