# TcpSettingsTcp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_challenge_ack** | **bool** | Allow arbitrary ACK in response to SYN? | [optional] 
**asymmetric_path** | **str** | Asymmetric path action | [optional] 
**bypass_exceed_oo_queue** | **bool** | Forward segments exceeding TCP out-of-order queue? | [optional] 
**check_timestamp_option** | **bool** | Drop segments with null timestamp option? | [optional] 
**drop_zero_flag** | **bool** | Drop segments without flag? | [optional] 
**siptcp_cleartext_proxy** | **str** | SIP TCP cleartext action (&#x60;&#39;0&#39;&#x60; &#x3D; Always Off, &#x60;&#39;1&#39;&#x60; &#x3D; Always Enabled, &#x60;&#39;2&#39;&#x60; &#x3D; Automatically enable proxy when needed) | [optional] 
**strip_mptcp_option** | **bool** | Strip MPTCP option? | [optional] 
**tcp_retransmit_scan** | **bool** | TCP retransmit scan? | [optional] 
**urgent_data** | **str** | Urgent data flag action | [optional] 

## Example

```python
from scm.device_settings.models.tcp_settings_tcp import TcpSettingsTcp

# TODO update the JSON string below
json = "{}"
# create an instance of TcpSettingsTcp from a JSON string
tcp_settings_tcp_instance = TcpSettingsTcp.from_json(json)
# print the JSON string representation of the object
print(TcpSettingsTcp.to_json())

# convert the object into a dict
tcp_settings_tcp_dict = tcp_settings_tcp_instance.to_dict()
# create an instance of TcpSettingsTcp from a dict
tcp_settings_tcp_from_dict = TcpSettingsTcp.from_dict(tcp_settings_tcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


