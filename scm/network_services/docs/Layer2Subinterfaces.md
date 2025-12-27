# Layer2Subinterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Description | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | L2 sub-interface name | 
**parent_interface** | **str** | Parent interface | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**vlan_tag** | **str** | VLAN tag | 

## Example

```python
from scm_network_services.models.layer2_subinterfaces import Layer2Subinterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of Layer2Subinterfaces from a JSON string
layer2_subinterfaces_instance = Layer2Subinterfaces.from_json(json)
# print the JSON string representation of the object
print(Layer2Subinterfaces.to_json())

# convert the object into a dict
layer2_subinterfaces_dict = layer2_subinterfaces_instance.to_dict()
# create an instance of Layer2Subinterfaces from a dict
layer2_subinterfaces_from_dict = Layer2Subinterfaces.from_dict(layer2_subinterfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


