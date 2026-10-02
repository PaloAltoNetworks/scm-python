# ConnectorGroupStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anycast_ip** | **str** |  | [optional] 
**counts** | [**ConnectorGroupStatusCounts**](ConnectorGroupStatusCounts.md) |  | [optional] 
**pa_region** | **str** |  | [optional] 
**sw_version** | **str** |  | [optional] 
**token_active** | **str** |  | [optional] 
**token_secret** | **str** |  | [optional] 
**user_id_ip** | **str** |  | [optional] 
**user_id_port** | **str** |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_group_status import ConnectorGroupStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroupStatus from a JSON string
connector_group_status_instance = ConnectorGroupStatus.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroupStatus.to_json())

# convert the object into a dict
connector_group_status_dict = connector_group_status_instance.to_dict()
# create an instance of ConnectorGroupStatus from a dict
connector_group_status_from_dict = ConnectorGroupStatus.from_dict(connector_group_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


