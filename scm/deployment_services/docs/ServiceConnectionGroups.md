# ServiceConnectionGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_snat** | **bool** |  | [optional] 
**id** | **str** | The UUID of the service connection group | [readonly] 
**name** | **str** |  | 
**pbf_only** | **bool** |  | [optional] 
**target** | **List[str]** |  | 

## Example

```python
from scm.deployment_services.models.service_connection_groups import ServiceConnectionGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnectionGroups from a JSON string
service_connection_groups_instance = ServiceConnectionGroups.from_json(json)
# print the JSON string representation of the object
print(ServiceConnectionGroups.to_json())

# convert the object into a dict
service_connection_groups_dict = service_connection_groups_instance.to_dict()
# create an instance of ServiceConnectionGroups from a dict
service_connection_groups_from_dict = ServiceConnectionGroups.from_dict(service_connection_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


