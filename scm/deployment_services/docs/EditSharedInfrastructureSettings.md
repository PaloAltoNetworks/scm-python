# EditSharedInfrastructureSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_application_blocks** | [**EditSharedInfrastructureSettingsConnectorApplicationBlocks**](EditSharedInfrastructureSettingsConnectorApplicationBlocks.md) |  | [optional] 
**connector_connector_blocks** | [**EditSharedInfrastructureSettingsConnectorConnectorBlocks**](EditSharedInfrastructureSettingsConnectorConnectorBlocks.md) |  | [optional] 
**egress_ip_notification_url** | **str** |  | [optional] 
**infra_bgp_as** | **str** |  | [optional] 
**infrastructure_subnet** | **str** |  | [optional] 
**infrastructure_subnet_ipv6** | **str** |  | [optional] 

## Example

```python
from scm_deployment_services.models.edit_shared_infrastructure_settings import EditSharedInfrastructureSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditSharedInfrastructureSettings from a JSON string
edit_shared_infrastructure_settings_instance = EditSharedInfrastructureSettings.from_json(json)
# print the JSON string representation of the object
print(EditSharedInfrastructureSettings.to_json())

# convert the object into a dict
edit_shared_infrastructure_settings_dict = edit_shared_infrastructure_settings_instance.to_dict()
# create an instance of EditSharedInfrastructureSettings from a dict
edit_shared_infrastructure_settings_from_dict = EditSharedInfrastructureSettings.from_dict(edit_shared_infrastructure_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


