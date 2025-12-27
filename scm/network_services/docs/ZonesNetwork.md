# ZonesNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_packet_buffer_protection** | **bool** |  | [optional] 
**external** | **List[str]** |  | [optional] 
**layer2** | **List[str]** |  | [optional] 
**layer3** | **List[str]** |  | [optional] 
**log_setting** | **str** |  | [optional] 
**tap** | **List[str]** |  | [optional] 
**tunnel** | **object** |  | [optional] 
**virtual_wire** | **List[str]** |  | [optional] 
**zone_protection_profile** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.zones_network import ZonesNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ZonesNetwork from a JSON string
zones_network_instance = ZonesNetwork.from_json(json)
# print the JSON string representation of the object
print(ZonesNetwork.to_json())

# convert the object into a dict
zones_network_dict = zones_network_instance.to_dict()
# create an instance of ZonesNetwork from a dict
zones_network_from_dict = ZonesNetwork.from_dict(zones_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


