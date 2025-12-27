# Layer3SubinterfacesArpInner

Layer 3 sub Interfaces ARP configuration object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hw_address** | **str** | MAC address | [optional] 
**name** | **str** | IP address | [optional] 

## Example

```python
from scm.network_services.models.layer3_subinterfaces_arp_inner import Layer3SubinterfacesArpInner

# TODO update the JSON string below
json = "{}"
# create an instance of Layer3SubinterfacesArpInner from a JSON string
layer3_subinterfaces_arp_inner_instance = Layer3SubinterfacesArpInner.from_json(json)
# print the JSON string representation of the object
print(Layer3SubinterfacesArpInner.to_json())

# convert the object into a dict
layer3_subinterfaces_arp_inner_dict = layer3_subinterfaces_arp_inner_instance.to_dict()
# create an instance of Layer3SubinterfacesArpInner from a dict
layer3_subinterfaces_arp_inner_from_dict = Layer3SubinterfacesArpInner.from_dict(layer3_subinterfaces_arp_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


