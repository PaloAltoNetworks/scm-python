# ConnectorGroupConnectorsConnectors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**limit** | **int** |  | [optional] [default to 200]
**offset** | **int** |  | [optional] [default to 0]
**total** | **int** |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_group_connectors_connectors import ConnectorGroupConnectorsConnectors

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroupConnectorsConnectors from a JSON string
connector_group_connectors_connectors_instance = ConnectorGroupConnectorsConnectors.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroupConnectorsConnectors.to_json())

# convert the object into a dict
connector_group_connectors_connectors_dict = connector_group_connectors_connectors_instance.to_dict()
# create an instance of ConnectorGroupConnectorsConnectors from a dict
connector_group_connectors_connectors_from_dict = ConnectorGroupConnectorsConnectors.from_dict(connector_group_connectors_connectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


