# ConnectorStatusFlagsCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipsubnet_supported** | **bool** |  | [optional] 
**wildcard_supported** | **bool** |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_status_flags_capabilities import ConnectorStatusFlagsCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorStatusFlagsCapabilities from a JSON string
connector_status_flags_capabilities_instance = ConnectorStatusFlagsCapabilities.from_json(json)
# print the JSON string representation of the object
print(ConnectorStatusFlagsCapabilities.to_json())

# convert the object into a dict
connector_status_flags_capabilities_dict = connector_status_flags_capabilities_instance.to_dict()
# create an instance of ConnectorStatusFlagsCapabilities from a dict
connector_status_flags_capabilities_from_dict = ConnectorStatusFlagsCapabilities.from_dict(connector_status_flags_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


