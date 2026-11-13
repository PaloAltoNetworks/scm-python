# ConnectorStatusFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**ConnectorStatusFlagsCapabilities**](ConnectorStatusFlagsCapabilities.md) |  | [optional] 
**config_state** | **str** |  | [optional] 
**control_plane_up** | **bool** |  | [optional] 
**token_state** | **str** |  | [optional] 
**tunnel_up** | **bool** |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_status_flags import ConnectorStatusFlags

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorStatusFlags from a JSON string
connector_status_flags_instance = ConnectorStatusFlags.from_json(json)
# print the JSON string representation of the object
print(ConnectorStatusFlags.to_json())

# convert the object into a dict
connector_status_flags_dict = connector_status_flags_instance.to_dict()
# create an instance of ConnectorStatusFlags from a dict
connector_status_flags_from_dict = ConnectorStatusFlags.from_dict(connector_status_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


