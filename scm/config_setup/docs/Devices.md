# Devices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_virus_version** | **str** |  | [optional] [readonly] 
**app_release_date** | **str** |  | [optional] [readonly] 
**app_version** | **str** |  | [optional] [readonly] 
**av_release_date** | **str** |  | [optional] [readonly] 
**available_licensess** | [**List[DevicesAvailableLicensessInner]**](DevicesAvailableLicensessInner.md) |  | [optional] [readonly] 
**connected_since** | **datetime** |  | [optional] [readonly] 
**description** | **str** | The description of the device | [optional] 
**dev_cert_detail** | **str** |  | [optional] [readonly] 
**dev_cert_expiry_date** | **str** |  | [optional] [readonly] 
**display_name** | **str** | The display name of the device | [optional] 
**family** | **str** | The product family of the device | [optional] [readonly] 
**folder** | **str** | The folder containing the device | 
**gp_client_verion** | **str** |  | [optional] [readonly] 
**gp_data_version** | **str** |  | [optional] [readonly] 
**ha_peer_serial** | **str** |  | [optional] [readonly] 
**ha_peer_state** | **str** |  | [optional] [readonly] 
**ha_state** | **str** |  | [optional] [readonly] 
**hostname** | **str** | The hostname of the device | [optional] [readonly] 
**id** | **str** | The UUID of the device | [readonly] 
**installed_licenses** | [**List[DevicesInstalledLicensesInner]**](DevicesInstalledLicensesInner.md) |  | [optional] [readonly] 
**iot_release_date** | **str** |  | [optional] [readonly] 
**iot_version** | **str** |  | [optional] [readonly] 
**ip_v6_address** | **str** | The IPv6 address of the device | [optional] [readonly] 
**ip_address** | **str** | The IPv4 address of the device | [optional] [readonly] 
**is_connected** | **bool** |  | [optional] [readonly] 
**labels** | **List[str]** | Labels assigned to the device | [optional] 
**license_match** | **bool** |  | [optional] [readonly] 
**log_db_version** | **str** |  | [optional] [readonly] 
**mac_address** | **str** | The MAC address of the device | [optional] [readonly] 
**model** | **str** | The model of the device | [optional] [readonly] 
**name** | **str** | The name of the device | 
**snippets** | **List[str]** | Snippets associated with the device | [optional] 
**software_version** | **str** |  | [optional] [readonly] 
**threat_release_date** | **str** |  | [optional] [readonly] 
**threat_version** | **str** |  | [optional] [readonly] 
**uptime** | **str** |  | [optional] [readonly] 
**url_db_type** | **str** |  | [optional] [readonly] 
**url_db_ver** | **str** |  | [optional] [readonly] 
**vm_state** | **str** |  | [optional] [readonly] 
**wf_release_date** | **str** |  | [optional] [readonly] 
**wf_ver** | **str** |  | [optional] [readonly] 

## Example

```python
from scm.config_setup.models.devices import Devices

# TODO update the JSON string below
json = "{}"
# create an instance of Devices from a JSON string
devices_instance = Devices.from_json(json)
# print the JSON string representation of the object
print(Devices.to_json())

# convert the object into a dict
devices_dict = devices_instance.to_dict()
# create an instance of Devices from a dict
devices_from_dict = Devices.from_dict(devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


