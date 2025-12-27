# ApplicationGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [readonly] 
**members** | **List[str]** |  | 
**name** | **str** | Alphanumeric string [ 0-9a-zA-Z._-] | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_objects.models.application_groups import ApplicationGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationGroups from a JSON string
application_groups_instance = ApplicationGroups.from_json(json)
# print the JSON string representation of the object
print(ApplicationGroups.to_json())

# convert the object into a dict
application_groups_dict = application_groups_instance.to_dict()
# create an instance of ApplicationGroups from a dict
application_groups_from_dict = ApplicationGroups.from_dict(application_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


