# ConnectorGroupConnectors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectors** | [**ConnectorGroupConnectorsConnectors**](ConnectorGroupConnectorsConnectors.md) |  | [optional] 
**group** | [**ConnectorGroups**](ConnectorGroups.md) |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_group_connectors import ConnectorGroupConnectors

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroupConnectors from a JSON string
connector_group_connectors_instance = ConnectorGroupConnectors.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroupConnectors.to_json())

# convert the object into a dict
connector_group_connectors_dict = connector_group_connectors_instance.to_dict()
# create an instance of ConnectorGroupConnectors from a dict
connector_group_connectors_from_dict = ConnectorGroupConnectors.from_dict(connector_group_connectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


