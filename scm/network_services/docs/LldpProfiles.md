# LldpProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**mode** | **str** | LLDP mode | [optional] 
**name** | **str** | LLDP profile name | 
**option_tlvs** | [**LldpProfilesOptionTlvs**](LldpProfilesOptionTlvs.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**snmp_syslog_notification** | **bool** | SNMP syslog notification | [optional] 

## Example

```python
from scm.network_services.models.lldp_profiles import LldpProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of LldpProfiles from a JSON string
lldp_profiles_instance = LldpProfiles.from_json(json)
# print the JSON string representation of the object
print(LldpProfiles.to_json())

# convert the object into a dict
lldp_profiles_dict = lldp_profiles_instance.to_dict()
# create an instance of LldpProfiles from a dict
lldp_profiles_from_dict = LldpProfiles.from_dict(lldp_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


