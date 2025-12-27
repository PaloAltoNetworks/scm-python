# DosProtectionProfilesFloodIcmp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] [default to False]
**red** | [**DosProtectionProfilesFloodIcmpRed**](DosProtectionProfilesFloodIcmpRed.md) |  | [optional] 

## Example

```python
from scm_security_services.models.dos_protection_profiles_flood_icmp import DosProtectionProfilesFloodIcmp

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionProfilesFloodIcmp from a JSON string
dos_protection_profiles_flood_icmp_instance = DosProtectionProfilesFloodIcmp.from_json(json)
# print the JSON string representation of the object
print(DosProtectionProfilesFloodIcmp.to_json())

# convert the object into a dict
dos_protection_profiles_flood_icmp_dict = dos_protection_profiles_flood_icmp_instance.to_dict()
# create an instance of DosProtectionProfilesFloodIcmp from a dict
dos_protection_profiles_flood_icmp_from_dict = DosProtectionProfilesFloodIcmp.from_dict(dos_protection_profiles_flood_icmp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


