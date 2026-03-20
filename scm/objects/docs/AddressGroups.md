# AddressGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**dynamic** | [**AddressGroupsDynamic**](AddressGroupsDynamic.md) |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the address group | [readonly] 
**name** | **str** | The name of the address group | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**static** | **List[str]** |  | [optional] 
**tag** | **List[str]** | Tags for address group object | [optional] 

## Example

```python
from scm.objects.models.address_groups import AddressGroups

# TODO update the JSON string below
json = "{}"
# create an instance of AddressGroups from a JSON string
address_groups_instance = AddressGroups.from_json(json)
# print the JSON string representation of the object
print(AddressGroups.to_json())

# convert the object into a dict
address_groups_dict = address_groups_instance.to_dict()
# create an instance of AddressGroups from a dict
address_groups_from_dict = AddressGroups.from_dict(address_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


