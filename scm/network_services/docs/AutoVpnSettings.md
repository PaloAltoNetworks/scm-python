# AutoVpnSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_range** | [**AutoVpnSettingsAsRange**](AutoVpnSettingsAsRange.md) |  | 
**enable_mesh_between_hubs** | **bool** | Enable mesh connection between hubs? | [optional] 
**vpn_address_pool** | **List[str]** | VPN address pool | 

## Example

```python
from scm.network_services.models.auto_vpn_settings import AutoVpnSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnSettings from a JSON string
auto_vpn_settings_instance = AutoVpnSettings.from_json(json)
# print the JSON string representation of the object
print(AutoVpnSettings.to_json())

# convert the object into a dict
auto_vpn_settings_dict = auto_vpn_settings_instance.to_dict()
# create an instance of AutoVpnSettings from a dict
auto_vpn_settings_from_dict = AutoVpnSettings.from_dict(auto_vpn_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


