# ConnectorGroupSubnetRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**ConnectorGroups**](ConnectorGroups.md) |  | [optional] 
**subnets** | [**ConnectorGroupConnectorsConnectors**](ConnectorGroupConnectorsConnectors.md) |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_group_subnet_rules import ConnectorGroupSubnetRules

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroupSubnetRules from a JSON string
connector_group_subnet_rules_instance = ConnectorGroupSubnetRules.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroupSubnetRules.to_json())

# convert the object into a dict
connector_group_subnet_rules_dict = connector_group_subnet_rules_instance.to_dict()
# create an instance of ConnectorGroupSubnetRules from a dict
connector_group_subnet_rules_from_dict = ConnectorGroupSubnetRules.from_dict(connector_group_subnet_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


