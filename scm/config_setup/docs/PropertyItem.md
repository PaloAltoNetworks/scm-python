# PropertyItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from scm_config_setup.models.property_item import PropertyItem

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyItem from a JSON string
property_item_instance = PropertyItem.from_json(json)
# print the JSON string representation of the object
print(PropertyItem.to_json())

# convert the object into a dict
property_item_dict = property_item_instance.to_dict()
# create an instance of PropertyItem from a dict
property_item_from_dict = PropertyItem.from_dict(property_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


