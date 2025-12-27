# DosProtectionProfilesFlood


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icmp** | [**DosProtectionProfilesFloodIcmp**](DosProtectionProfilesFloodIcmp.md) |  | [optional] 
**icmpv6** | [**DosProtectionProfilesFloodIcmp**](DosProtectionProfilesFloodIcmp.md) |  | [optional] 
**other_ip** | [**DosProtectionProfilesFloodIcmp**](DosProtectionProfilesFloodIcmp.md) |  | [optional] 
**tcp_syn** | [**DosProtectionProfilesFloodTcpSyn**](DosProtectionProfilesFloodTcpSyn.md) |  | [optional] 
**udp** | [**DosProtectionProfilesFloodIcmp**](DosProtectionProfilesFloodIcmp.md) |  | [optional] 

## Example

```python
from scm.security_services.models.dos_protection_profiles_flood import DosProtectionProfilesFlood

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionProfilesFlood from a JSON string
dos_protection_profiles_flood_instance = DosProtectionProfilesFlood.from_json(json)
# print the JSON string representation of the object
print(DosProtectionProfilesFlood.to_json())

# convert the object into a dict
dos_protection_profiles_flood_dict = dos_protection_profiles_flood_instance.to_dict()
# create an instance of DosProtectionProfilesFlood from a dict
dos_protection_profiles_flood_from_dict = DosProtectionProfilesFlood.from_dict(dos_protection_profiles_flood_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


