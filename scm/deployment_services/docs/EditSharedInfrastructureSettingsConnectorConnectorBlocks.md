# EditSharedInfrastructureSettingsConnectorConnectorBlocks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | **List[str]** | Array of CIDR blocks for connector-to-connector communication | [optional] 

## Example

```python
from scm.deployment_services.models.edit_shared_infrastructure_settings_connector_connector_blocks import EditSharedInfrastructureSettingsConnectorConnectorBlocks

# TODO update the JSON string below
json = "{}"
# create an instance of EditSharedInfrastructureSettingsConnectorConnectorBlocks from a JSON string
edit_shared_infrastructure_settings_connector_connector_blocks_instance = EditSharedInfrastructureSettingsConnectorConnectorBlocks.from_json(json)
# print the JSON string representation of the object
print(EditSharedInfrastructureSettingsConnectorConnectorBlocks.to_json())

# convert the object into a dict
edit_shared_infrastructure_settings_connector_connector_blocks_dict = edit_shared_infrastructure_settings_connector_connector_blocks_instance.to_dict()
# create an instance of EditSharedInfrastructureSettingsConnectorConnectorBlocks from a dict
edit_shared_infrastructure_settings_connector_connector_blocks_from_dict = EditSharedInfrastructureSettingsConnectorConnectorBlocks.from_dict(edit_shared_infrastructure_settings_connector_connector_blocks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


