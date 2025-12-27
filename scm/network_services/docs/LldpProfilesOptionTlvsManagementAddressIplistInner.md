# LldpProfilesOptionTlvsManagementAddressIplistInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | Interface | [optional] 
**ipv4** | **str** | IPv4 Address | [optional] 
**ipv6** | **str** | IPv6 Address | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from scm_network_services.models.lldp_profiles_option_tlvs_management_address_iplist_inner import LldpProfilesOptionTlvsManagementAddressIplistInner

# TODO update the JSON string below
json = "{}"
# create an instance of LldpProfilesOptionTlvsManagementAddressIplistInner from a JSON string
lldp_profiles_option_tlvs_management_address_iplist_inner_instance = LldpProfilesOptionTlvsManagementAddressIplistInner.from_json(json)
# print the JSON string representation of the object
print(LldpProfilesOptionTlvsManagementAddressIplistInner.to_json())

# convert the object into a dict
lldp_profiles_option_tlvs_management_address_iplist_inner_dict = lldp_profiles_option_tlvs_management_address_iplist_inner_instance.to_dict()
# create an instance of LldpProfilesOptionTlvsManagementAddressIplistInner from a dict
lldp_profiles_option_tlvs_management_address_iplist_inner_from_dict = LldpProfilesOptionTlvsManagementAddressIplistInner.from_dict(lldp_profiles_option_tlvs_management_address_iplist_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


