# AutoTagActionsActionsInnerTypeTagging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Add or Remove tag option | 
**tags** | **List[str]** | Tags for address object | [optional] 
**target** | **str** | Source or Destination Address, User, X-Forwarded-For Address | 
**timeout** | **int** |  | [optional] 

## Example

```python
from scm.objects.models.auto_tag_actions_actions_inner_type_tagging import AutoTagActionsActionsInnerTypeTagging

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTagActionsActionsInnerTypeTagging from a JSON string
auto_tag_actions_actions_inner_type_tagging_instance = AutoTagActionsActionsInnerTypeTagging.from_json(json)
# print the JSON string representation of the object
print(AutoTagActionsActionsInnerTypeTagging.to_json())

# convert the object into a dict
auto_tag_actions_actions_inner_type_tagging_dict = auto_tag_actions_actions_inner_type_tagging_instance.to_dict()
# create an instance of AutoTagActionsActionsInnerTypeTagging from a dict
auto_tag_actions_actions_inner_type_tagging_from_dict = AutoTagActionsActionsInnerTypeTagging.from_dict(auto_tag_actions_actions_inner_type_tagging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


