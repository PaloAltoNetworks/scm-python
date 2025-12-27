# SharedInfrastructureSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**captive_portal_redirect_ip_address** | **str** |  | [optional] 
**connector_application_blocks** | [**EditSharedInfrastructureSettingsConnectorApplicationBlocks**](EditSharedInfrastructureSettingsConnectorApplicationBlocks.md) |  | [optional] 
**connector_connector_blocks** | [**EditSharedInfrastructureSettingsConnectorConnectorBlocks**](EditSharedInfrastructureSettingsConnectorConnectorBlocks.md) |  | [optional] 
**egress_ip_notification_url** | **str** |  | [optional] 
**folder** | **str** | The folder containing the shared infrastructure settings | [optional] [readonly] [default to 'Shared']
**infra_bgp_as** | **str** |  | [optional] 
**infrastructure_subnet** | **str** |  | [optional] 
**infrastructure_subnet_ipv6** | **str** |  | [optional] 
**ipv6** | **bool** |  | [optional] 
**loopback_ips** | **List[str]** |  | [optional] 
**tunnel_monitor_ip_address** | **str** |  | [optional] 

## Example

```python
from scm.deployment_services.models.shared_infrastructure_settings import SharedInfrastructureSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SharedInfrastructureSettings from a JSON string
shared_infrastructure_settings_instance = SharedInfrastructureSettings.from_json(json)
# print the JSON string representation of the object
print(SharedInfrastructureSettings.to_json())

# convert the object into a dict
shared_infrastructure_settings_dict = shared_infrastructure_settings_instance.to_dict()
# create an instance of SharedInfrastructureSettings from a dict
shared_infrastructure_settings_from_dict = SharedInfrastructureSettings.from_dict(shared_infrastructure_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


