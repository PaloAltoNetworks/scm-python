# ZoneProtectionProfilesFloodTcpSynSynCookies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_rate** | **int** | When the flow exceeds the &#x60;activate_rate&#x60;&#x60; threshold, the firewall drops individual SYN packets randomly to restrict the flow. | 
**alarm_rate** | **int** | When the flow exceeds the &#x60;alert_rate&#x60;&#x60; threshold, an alarm is generated. | 
**maximal_rate** | **int** | When the flow exceeds the &#x60;maximal_rate&#x60; threshold, 100% of incoming SYN packets are dropped. | 

## Example

```python
from scm.network_services.models.zone_protection_profiles_flood_tcp_syn_syn_cookies import ZoneProtectionProfilesFloodTcpSynSynCookies

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesFloodTcpSynSynCookies from a JSON string
zone_protection_profiles_flood_tcp_syn_syn_cookies_instance = ZoneProtectionProfilesFloodTcpSynSynCookies.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesFloodTcpSynSynCookies.to_json())

# convert the object into a dict
zone_protection_profiles_flood_tcp_syn_syn_cookies_dict = zone_protection_profiles_flood_tcp_syn_syn_cookies_instance.to_dict()
# create an instance of ZoneProtectionProfilesFloodTcpSynSynCookies from a dict
zone_protection_profiles_flood_tcp_syn_syn_cookies_from_dict = ZoneProtectionProfilesFloodTcpSynSynCookies.from_dict(zone_protection_profiles_flood_tcp_syn_syn_cookies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


