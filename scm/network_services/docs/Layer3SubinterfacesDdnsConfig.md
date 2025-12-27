# Layer3SubinterfacesDdnsConfig

Dynamic DNS configuration specific to the Layer 3 sub Interfaces.

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
from scm.network_services.models.layer3_subinterfaces_ddns_config import Layer3SubinterfacesDdnsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of Layer3SubinterfacesDdnsConfig from a JSON string
layer3_subinterfaces_ddns_config_instance = Layer3SubinterfacesDdnsConfig.from_json(json)
# print the JSON string representation of the object
print(Layer3SubinterfacesDdnsConfig.to_json())

# convert the object into a dict
layer3_subinterfaces_ddns_config_dict = layer3_subinterfaces_ddns_config_instance.to_dict()
# create an instance of Layer3SubinterfacesDdnsConfig from a dict
layer3_subinterfaces_ddns_config_from_dict = Layer3SubinterfacesDdnsConfig.from_dict(layer3_subinterfaces_ddns_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


