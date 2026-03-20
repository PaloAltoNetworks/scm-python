# AutoTagActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[AutoTagActionsActionsInner]**](AutoTagActionsActionsInner.md) |  | [optional] 
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**filter** | **str** | Tag based filter defining group membership e.g. &#x60;tag1 AND tag2 OR tag3&#x60; | 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**log_type** | **str** |  | [readonly] 
**name** | **str** | Alphanumeric string [ 0-9a-zA-Z._-] | 
**quarantine** | **bool** |  | [optional] 
**send_to_panorama** | **bool** |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.objects.models.auto_tag_actions import AutoTagActions

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTagActions from a JSON string
auto_tag_actions_instance = AutoTagActions.from_json(json)
# print the JSON string representation of the object
print(AutoTagActions.to_json())

# convert the object into a dict
auto_tag_actions_dict = auto_tag_actions_instance.to_dict()
# create an instance of AutoTagActions from a dict
auto_tag_actions_from_dict = AutoTagActions.from_dict(auto_tag_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


