# SessionSettingsSessionSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerated_aging_enable** | **bool** | Enable accelerated aging | [optional] [default to True]
**accelerated_aging_scaling_factor** | **float** | Accelerated aging scaling factor | [optional] [default to 2]
**accelerated_aging_threshold** | **float** | Accelerated aging threshold | [optional] [default to 80]
**config** | [**SessionSettingsSessionSettingsConfig**](SessionSettingsSessionSettingsConfig.md) |  | [optional] 
**dhcp_bcast_session_on** | **bool** | Enable DHCP broadcast session | [optional] [default to False]
**erspan** | **bool** | Enable ERSPAN support | [optional] [default to False]
**icmp_unreachable_rate** | **float** | ICMP unreachable packet rate (per second) | [optional] [default to 200]
**icmpv6_rate_limit** | [**SessionSettingsSessionSettingsIcmpv6RateLimit**](SessionSettingsSessionSettingsIcmpv6RateLimit.md) |  | [optional] 
**ipv6_firewalling** | **bool** | Enable IPv6 firewalling | [optional] [default to True]
**jumbo_frame** | [**SessionSettingsSessionSettingsJumboFrame**](SessionSettingsSessionSettingsJumboFrame.md) |  | [optional] 
**max_pending_mcast_pkts_per_session** | **float** | Multicast route setup buffer size | [optional] [default to 1000]
**multicast_route_setup_buffering** | **bool** | Multicast route setup buffering | [optional] [default to False]
**nat** | [**SessionSettingsSessionSettingsNat**](SessionSettingsSessionSettingsNat.md) |  | [optional] 
**nat64** | [**SessionSettingsSessionSettingsNat64**](SessionSettingsSessionSettingsNat64.md) |  | [optional] 
**packet_buffer_protection_activate** | **float** | Activate (%) | [optional] [default to 80]
**packet_buffer_protection_alert** | **int** | Alert (%) | [optional] [default to 50]
**packet_buffer_protection_block_countdown** | **float** | Block countdown threshold (%) | [optional] [default to 80]
**packet_buffer_protection_block_duration_time** | **float** | Block duration (seconds) | [optional] [default to 3600]
**packet_buffer_protection_block_hold_time** | **float** | Block hold time (seconds) | [optional] [default to 60]
**packet_buffer_protection_enable** | **bool** | Enable packet buffer protection | [optional] [default to True]
**packet_buffer_protection_latency_activate** | **float** | Latency activate (milliseconds) | [optional] [default to 200]
**packet_buffer_protection_latency_alert** | **float** | Latency alert (milliseconds) | [optional] [default to 50]
**packet_buffer_protection_latency_block_countdown** | **float** | Block countdown threshold (milliseconds) | [optional] [default to 500]
**packet_buffer_protection_latency_max_tolerate** | **float** | Latency max tolerate (milliseconds) | [optional] [default to 500]
**packet_buffer_protection_monitor_only** | **bool** | Packet buffer protection monitor only | [optional] [default to False]
**packet_buffer_protection_use_latency** | **bool** | Enabled latency-based activation | [optional] [default to False]

## Example

```python
from scm.device_settings.models.session_settings_session_settings import SessionSettingsSessionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSettingsSessionSettings from a JSON string
session_settings_session_settings_instance = SessionSettingsSessionSettings.from_json(json)
# print the JSON string representation of the object
print(SessionSettingsSessionSettings.to_json())

# convert the object into a dict
session_settings_session_settings_dict = session_settings_session_settings_instance.to_dict()
# create an instance of SessionSettingsSessionSettings from a dict
session_settings_session_settings_from_dict = SessionSettingsSessionSettings.from_dict(session_settings_session_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


