# GeneralSettingsGeneral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_login_banner** | **bool** | Force admins to acknowledge login banner | [optional] [default to False]
**domain** | **str** | DNS domain | [optional] 
**geo_location** | [**GeneralSettingsGeneralGeoLocation**](GeneralSettingsGeneralGeoLocation.md) |  | [optional] 
**locale** | **str** | Locale | [optional] [default to 'en']
**login_banner** | **str** | Logon banner | [optional] 
**setting** | [**GeneralSettingsGeneralSetting**](GeneralSettingsGeneralSetting.md) |  | [optional] 
**ssl_tls_service_profile** | **str** | SSL/TLS service profile | [optional] 
**timezone** | **str** | Timezone | [optional] 

## Example

```python
from scm.device_settings.models.general_settings_general import GeneralSettingsGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralSettingsGeneral from a JSON string
general_settings_general_instance = GeneralSettingsGeneral.from_json(json)
# print the JSON string representation of the object
print(GeneralSettingsGeneral.to_json())

# convert the object into a dict
general_settings_general_dict = general_settings_general_instance.to_dict()
# create an instance of GeneralSettingsGeneral from a dict
general_settings_general_from_dict = GeneralSettingsGeneral.from_dict(general_settings_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


