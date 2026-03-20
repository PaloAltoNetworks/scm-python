# LldpProfilesOptionTlvs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**management_address** | [**LldpProfilesOptionTlvsManagementAddress**](LldpProfilesOptionTlvsManagementAddress.md) |  | [optional] 
**port_description** | **bool** | Option TLV Port Description | [optional] 
**system_capabilities** | **bool** | Option TLV System Capabilities | [optional] 
**system_description** | **bool** | Option TLV System Description | [optional] 
**system_name** | **bool** | Option TLV System Name | [optional] 

## Example

```python
from scm.network_services.models.lldp_profiles_option_tlvs import LldpProfilesOptionTlvs

# TODO update the JSON string below
json = "{}"
# create an instance of LldpProfilesOptionTlvs from a JSON string
lldp_profiles_option_tlvs_instance = LldpProfilesOptionTlvs.from_json(json)
# print the JSON string representation of the object
print(LldpProfilesOptionTlvs.to_json())

# convert the object into a dict
lldp_profiles_option_tlvs_dict = lldp_profiles_option_tlvs_instance.to_dict()
# create an instance of LldpProfilesOptionTlvs from a dict
lldp_profiles_option_tlvs_from_dict = LldpProfilesOptionTlvs.from_dict(lldp_profiles_option_tlvs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


