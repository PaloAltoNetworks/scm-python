# EthernetInterfacesLayer3DdnsConfig

Dynamic DNS configuration specific to the Ethernet Interfaces.

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
from scm_network_services.models.ethernet_interfaces_layer3_ddns_config import EthernetInterfacesLayer3DdnsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfacesLayer3DdnsConfig from a JSON string
ethernet_interfaces_layer3_ddns_config_instance = EthernetInterfacesLayer3DdnsConfig.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfacesLayer3DdnsConfig.to_json())

# convert the object into a dict
ethernet_interfaces_layer3_ddns_config_dict = ethernet_interfaces_layer3_ddns_config_instance.to_dict()
# create an instance of EthernetInterfacesLayer3DdnsConfig from a dict
ethernet_interfaces_layer3_ddns_config_from_dict = EthernetInterfacesLayer3DdnsConfig.from_dict(ethernet_interfaces_layer3_ddns_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


