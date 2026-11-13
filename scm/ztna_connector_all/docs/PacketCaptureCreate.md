# PacketCaptureCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | IPv4 address | [optional] 
**interface** | **str** | Following are the acceptable labels - internal, external, tunnel | 
**port** | **str** | Port number | [optional] 
**protocol** | **str** | Following are the acceptable labels - TCP, UDP, ICMP, ARP | [optional] 

## Example

```python
from scm.ztna_connector_all.models.packet_capture_create import PacketCaptureCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PacketCaptureCreate from a JSON string
packet_capture_create_instance = PacketCaptureCreate.from_json(json)
# print the JSON string representation of the object
print(PacketCaptureCreate.to_json())

# convert the object into a dict
packet_capture_create_dict = packet_capture_create_instance.to_dict()
# create an instance of PacketCaptureCreate from a dict
packet_capture_create_from_dict = PacketCaptureCreate.from_dict(packet_capture_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


