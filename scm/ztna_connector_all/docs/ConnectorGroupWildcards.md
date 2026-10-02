# ConnectorGroupWildcards


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**ConnectorGroups**](ConnectorGroups.md) |  | [optional] 
**wildcards** | [**ConnectorGroupConnectorsConnectors**](ConnectorGroupConnectorsConnectors.md) |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_group_wildcards import ConnectorGroupWildcards

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroupWildcards from a JSON string
connector_group_wildcards_instance = ConnectorGroupWildcards.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroupWildcards.to_json())

# convert the object into a dict
connector_group_wildcards_dict = connector_group_wildcards_instance.to_dict()
# create an instance of ConnectorGroupWildcards from a dict
connector_group_wildcards_from_dict = ConnectorGroupWildcards.from_dict(connector_group_wildcards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


