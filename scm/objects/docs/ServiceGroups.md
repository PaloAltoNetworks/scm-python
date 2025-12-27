# ServiceGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the service group | [readonly] 
**members** | **List[str]** |  | 
**name** | **str** | The name of the service group | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**tag** | **List[str]** | Tags associated with the service group | [optional] 

## Example

```python
from scm_objects.models.service_groups import ServiceGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceGroups from a JSON string
service_groups_instance = ServiceGroups.from_json(json)
# print the JSON string representation of the object
print(ServiceGroups.to_json())

# convert the object into a dict
service_groups_dict = service_groups_instance.to_dict()
# create an instance of ServiceGroups from a dict
service_groups_from_dict = ServiceGroups.from_dict(service_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


