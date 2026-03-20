# SdwanSaasQualityProfilesMonitorModeStaticIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | [**SdwanSaasQualityProfilesMonitorModeStaticIpFqdn**](SdwanSaasQualityProfilesMonitorModeStaticIpFqdn.md) |  | [optional] 
**ip_address** | [**List[SdwanSaasQualityProfilesMonitorModeStaticIpIpAddressInner]**](SdwanSaasQualityProfilesMonitorModeStaticIpIpAddressInner.md) | List of IP addresses | [optional] 

## Example

```python
from scm.network_services.models.sdwan_saas_quality_profiles_monitor_mode_static_ip import SdwanSaasQualityProfilesMonitorModeStaticIp

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanSaasQualityProfilesMonitorModeStaticIp from a JSON string
sdwan_saas_quality_profiles_monitor_mode_static_ip_instance = SdwanSaasQualityProfilesMonitorModeStaticIp.from_json(json)
# print the JSON string representation of the object
print(SdwanSaasQualityProfilesMonitorModeStaticIp.to_json())

# convert the object into a dict
sdwan_saas_quality_profiles_monitor_mode_static_ip_dict = sdwan_saas_quality_profiles_monitor_mode_static_ip_instance.to_dict()
# create an instance of SdwanSaasQualityProfilesMonitorModeStaticIp from a dict
sdwan_saas_quality_profiles_monitor_mode_static_ip_from_dict = SdwanSaasQualityProfilesMonitorModeStaticIp.from_dict(sdwan_saas_quality_profiles_monitor_mode_static_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


