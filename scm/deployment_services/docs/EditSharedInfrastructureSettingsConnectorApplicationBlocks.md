# EditSharedInfrastructureSettingsConnectorApplicationBlocks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | **List[str]** | Array of CIDR blocks for connector-to-application communication | [optional] 

## Example

```python
from scm_deployment_services.models.edit_shared_infrastructure_settings_connector_application_blocks import EditSharedInfrastructureSettingsConnectorApplicationBlocks

# TODO update the JSON string below
json = "{}"
# create an instance of EditSharedInfrastructureSettingsConnectorApplicationBlocks from a JSON string
edit_shared_infrastructure_settings_connector_application_blocks_instance = EditSharedInfrastructureSettingsConnectorApplicationBlocks.from_json(json)
# print the JSON string representation of the object
print(EditSharedInfrastructureSettingsConnectorApplicationBlocks.to_json())

# convert the object into a dict
edit_shared_infrastructure_settings_connector_application_blocks_dict = edit_shared_infrastructure_settings_connector_application_blocks_instance.to_dict()
# create an instance of EditSharedInfrastructureSettingsConnectorApplicationBlocks from a dict
edit_shared_infrastructure_settings_connector_application_blocks_from_dict = EditSharedInfrastructureSettingsConnectorApplicationBlocks.from_dict(edit_shared_infrastructure_settings_connector_application_blocks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


