# ConnectorGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **str** |  | [optional] [readonly] 
**description** | **str** | Description of the connector group. | [optional] 
**is_autoscale** | **bool** | Whether the connector group is autoscaled.  If omitted, defaults to false. | [optional] 
**is_ngfw** | **bool** | Connector group type.  If false (default), the group is a ZTNA Connector group. If true, the group is an NGFW Connector group.  If omitted, defaults to false. | [optional] 
**name** | **str** | Name of the connector group.  It can only be 64 characters long and contain unicode text, space, dash, or underscore, or period. | 
**oid** | **str** | Connector Group ID | [optional] [readonly] 
**pba_project_name** | **str** | DPA project name that this connector group will serve.  This field must be provided when the tenant is DPA-enabled, and must not be provided when the tenant is not DPA-enabled. | [optional] 
**preserve_user_id** | **bool** | Whether to preserve user ID for this connector group.  If omitted, defaults to false. | [optional] 
**updated_time** | **str** |  | [optional] [readonly] 

## Example

```python
from scm.ztna_connector_all.models.connector_groups import ConnectorGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroups from a JSON string
connector_groups_instance = ConnectorGroups.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroups.to_json())

# convert the object into a dict
connector_groups_dict = connector_groups_instance.to_dict()
# create an instance of ConnectorGroups from a dict
connector_groups_from_dict = ConnectorGroups.from_dict(connector_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


