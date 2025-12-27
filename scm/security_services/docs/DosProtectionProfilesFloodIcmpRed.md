# DosProtectionProfilesFloodIcmpRed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_rate** | **int** | Connection rate (cps) to start RED | [default to 10000]
**alarm_rate** | **int** | Connection rate (cps) to generate alarm | [default to 10000]
**block** | [**DosProtectionProfilesFloodIcmpRedBlock**](DosProtectionProfilesFloodIcmpRedBlock.md) |  | [optional] 
**maximal_rate** | **int** | Maximal connection rate (cps) allowed | [default to 40000]

## Example

```python
from scm_security_services.models.dos_protection_profiles_flood_icmp_red import DosProtectionProfilesFloodIcmpRed

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionProfilesFloodIcmpRed from a JSON string
dos_protection_profiles_flood_icmp_red_instance = DosProtectionProfilesFloodIcmpRed.from_json(json)
# print the JSON string representation of the object
print(DosProtectionProfilesFloodIcmpRed.to_json())

# convert the object into a dict
dos_protection_profiles_flood_icmp_red_dict = dos_protection_profiles_flood_icmp_red_instance.to_dict()
# create an instance of DosProtectionProfilesFloodIcmpRed from a dict
dos_protection_profiles_flood_icmp_red_from_dict = DosProtectionProfilesFloodIcmpRed.from_dict(dos_protection_profiles_flood_icmp_red_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


