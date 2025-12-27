# VlanInterfacesDdnsConfig

Dynamic DNS configuration specific to the Vlan Interfaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddns_cert_profile** | **str** | Certificate profile | 
**ddns_enabled** | **bool** | Enable DDNS? | [optional] [default to False]
**ddns_hostname** | **str** |  | 
**ddns_ip** | **str** | IP to register (static only) | [optional] 
**ddns_update_interval** | **int** | Update interval (days) | [optional] [default to 1]
**ddns_vendor** | **str** | DDNS vendor | 
**ddns_vendor_config** | **str** | DDNS vendor | 

## Example

```python
from scm_network_services.models.vlan_interfaces_ddns_config import VlanInterfacesDdnsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VlanInterfacesDdnsConfig from a JSON string
vlan_interfaces_ddns_config_instance = VlanInterfacesDdnsConfig.from_json(json)
# print the JSON string representation of the object
print(VlanInterfacesDdnsConfig.to_json())

# convert the object into a dict
vlan_interfaces_ddns_config_dict = vlan_interfaces_ddns_config_instance.to_dict()
# create an instance of VlanInterfacesDdnsConfig from a dict
vlan_interfaces_ddns_config_from_dict = VlanInterfacesDdnsConfig.from_dict(vlan_interfaces_ddns_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


