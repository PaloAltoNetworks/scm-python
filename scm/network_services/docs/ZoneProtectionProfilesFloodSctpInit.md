# ZoneProtectionProfilesFloodSctpInit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable protection against floods of Stream Control Transmission Protocol (SCTP) packets that contain an Initiation (INIT) chunk? | [optional] 
**red** | [**ZoneProtectionProfilesFloodSctpInitRed**](ZoneProtectionProfilesFloodSctpInitRed.md) |  | [optional] 

## Example

```python
from scm.network_services.models.zone_protection_profiles_flood_sctp_init import ZoneProtectionProfilesFloodSctpInit

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodSctpInit from a JSON string
zone_protection_profiles_flood_sctp_init_instance = ZoneProtectionProfilesFloodSctpInit.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodSctpInit.to_json())

# convert the object into a dict
zone_protection_profiles_flood_sctp_init_dict = zone_protection_profiles_flood_sctp_init_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodSctpInit from a dict
zone_protection_profiles_flood_sctp_init_from_dict = ZoneProtectionProfilesFloodSctpInit.from_dict(zone_protection_profiles_flood_sctp_init_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


