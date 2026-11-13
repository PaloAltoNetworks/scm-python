# ConnectorGroupStatusCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | **int** |  | [optional] 
**connectors** | **int** |  | [optional] 
**ipsubnets** | **int** |  | [optional] 
**wildcards** | **int** |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_group_status_counts import ConnectorGroupStatusCounts

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroupStatusCounts from a JSON string
connector_group_status_counts_instance = ConnectorGroupStatusCounts.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroupStatusCounts.to_json())

# convert the object into a dict
connector_group_status_counts_dict = connector_group_status_counts_instance.to_dict()
# create an instance of ConnectorGroupStatusCounts from a dict
connector_group_status_counts_from_dict = ConnectorGroupStatusCounts.from_dict(connector_group_status_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


