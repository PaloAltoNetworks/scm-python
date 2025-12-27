# LldpProfilesOptionTlvsManagementAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Management address enabled | [optional] 
**iplist** | [**List[LldpProfilesOptionTlvsManagementAddressIplistInner]**](LldpProfilesOptionTlvsManagementAddressIplistInner.md) |  | [optional] 

## Example

```python
from scm.network_services.models.lldp_profiles_option_tlvs_management_address import LldpProfilesOptionTlvsManagementAddress

# TODO update the JSON string below
json = "{}"
# create an instance of LldpProfilesOptionTlvsManagementAddress from a JSON string
lldp_profiles_option_tlvs_management_address_instance = LldpProfilesOptionTlvsManagementAddress.from_json(json)
# print the JSON string representation of the object
print(LldpProfilesOptionTlvsManagementAddress.to_json())

# convert the object into a dict
lldp_profiles_option_tlvs_management_address_dict = lldp_profiles_option_tlvs_management_address_instance.to_dict()
# create an instance of LldpProfilesOptionTlvsManagementAddress from a dict
lldp_profiles_option_tlvs_management_address_from_dict = LldpProfilesOptionTlvsManagementAddress.from_dict(lldp_profiles_option_tlvs_management_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


