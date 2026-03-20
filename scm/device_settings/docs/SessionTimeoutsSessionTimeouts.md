# SessionTimeoutsSessionTimeouts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout_captive_portal** | **int** | Captive Portal (seconds) | [optional] [default to 30]
**timeout_default** | **int** | Default timeout (seconds) | [optional] [default to 30]
**timeout_discard_default** | **int** | Discard default (seconds) | [optional] [default to 60]
**timeout_discard_tcp** | **int** | Discard TCP (seconds) | [optional] [default to 90]
**timeout_discard_udp** | **int** | Discard UDP (seconds) | [optional] [default to 60]
**timeout_icmp** | **int** | ICMP (seconds) | [optional] [default to 6]
**timeout_scan** | **int** | Scan (seconds) | [optional] [default to 10]
**timeout_tcp** | **int** | TCP (seconds) | [optional] [default to 3600]
**timeout_tcp_half_closed** | **int** | TCP Half Closed (seconds) | [optional] [default to 120]
**timeout_tcp_time_wait** | **int** | TCP Time Wait (seconds) | [optional] [default to 15]
**timeout_tcp_unverified_rst** | **int** | Unverified RST (seconds) | [optional] [default to 30]
**timeout_tcphandshake** | **int** | TCP handshake (seconds) | [optional] [default to 10]
**timeout_tcpinit** | **int** | TCP init (seconds) | [optional] [default to 5]
**timeout_udp** | **int** | UDP (seconds) | [optional] [default to 30]

## Example

```python
from scm.device_settings.models.session_timeouts_session_timeouts import SessionTimeoutsSessionTimeouts

# TODO update the JSON string below
json = "{}"
# create an instance of SessionTimeoutsSessionTimeouts from a JSON string
session_timeouts_session_timeouts_instance = SessionTimeoutsSessionTimeouts.from_json(json)
# print the JSON string representation of the object
print(SessionTimeoutsSessionTimeouts.to_json())

# convert the object into a dict
session_timeouts_session_timeouts_dict = session_timeouts_session_timeouts_instance.to_dict()
# create an instance of SessionTimeoutsSessionTimeouts from a dict
session_timeouts_session_timeouts_from_dict = SessionTimeoutsSessionTimeouts.from_dict(session_timeouts_session_timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


