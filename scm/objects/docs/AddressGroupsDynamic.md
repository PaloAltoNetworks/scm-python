# AddressGroupsDynamic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Tag based filter defining group membership | 

## Example

```python
from scm.objects.models.address_groups_dynamic import AddressGroupsDynamic

# TODO update the JSON string below
json = "{}"
# create an instance of AddressGroupsDynamic from a JSON string
address_groups_dynamic_instance = AddressGroupsDynamic.from_json(json)
# print the JSON string representation of the object
print(AddressGroupsDynamic.to_json())

# convert the object into a dict
address_groups_dynamic_dict = address_groups_dynamic_instance.to_dict()
# create an instance of AddressGroupsDynamic from a dict
address_groups_dynamic_from_dict = AddressGroupsDynamic.from_dict(address_groups_dynamic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


