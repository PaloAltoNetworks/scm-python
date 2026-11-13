# Connectors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **str** |  | [optional] [readonly] 
**description** | **str** | Description of the connector. | [optional] 
**group** | **str** | The connector group id | 
**name** | **str** | Name of the connector.  It can only be 64 characters long and contain unicode text, space, dash, or underscore, or period. | 
**oid** | **str** | Id of the entry. | [optional] [readonly] 
**updated_time** | **str** |  | [optional] [readonly] 

## Example

```python
from scm.ztna_connector_all.models.connectors import Connectors

# TODO update the JSON string below
json = "{}"
# create an instance of Connectors from a JSON string
connectors_instance = Connectors.from_json(json)
# print the JSON string representation of the object
print(Connectors.to_json())

# convert the object into a dict
connectors_dict = connectors_instance.to_dict()
# create an instance of Connectors from a dict
connectors_from_dict = Connectors.from_dict(connectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


