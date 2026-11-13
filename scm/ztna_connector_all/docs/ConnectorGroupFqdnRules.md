# ConnectorGroupFqdnRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**ConnectorGroupConnectorsConnectors**](ConnectorGroupConnectorsConnectors.md) |  | [optional] 
**group** | [**ConnectorGroups**](ConnectorGroups.md) |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_group_fqdn_rules import ConnectorGroupFqdnRules

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroupFqdnRules from a JSON string
connector_group_fqdn_rules_instance = ConnectorGroupFqdnRules.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroupFqdnRules.to_json())

# convert the object into a dict
connector_group_fqdn_rules_dict = connector_group_fqdn_rules_instance.to_dict()
# create an instance of ConnectorGroupFqdnRules from a dict
connector_group_fqdn_rules_from_dict = ConnectorGroupFqdnRules.from_dict(connector_group_fqdn_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


