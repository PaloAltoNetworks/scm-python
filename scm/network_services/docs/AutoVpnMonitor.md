# AutoVpnMonitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | Connection type | [optional] 
**destination_device** | **str** | Branch firewall serial number | [optional] 
**ike_gateway_name** | **str** | IKE gateway name | [optional] 
**ike_sa_result** | **str** | IKE security association result | [optional] 
**ike_sa_status** | **str** | IKE security association status | [optional] 
**ipsec_sa_result** | **str** | IPSec security association result | [optional] 
**ipsec_sa_status** | **str** | IPSec security association status | [optional] 
**local_intf** | **str** | Hub firewall interface | [optional] 
**peer_intf** | **str** | Branch firewall interface | [optional] 
**source_device** | **str** | Hub firewall serial number | [optional] 
**ts** | **str** | Timestamp | [optional] 
**tunnel_ip** | **str** | Hub tunnel IP address | [optional] 
**tunnel_name** | **str** | Tunnel name | [optional] 
**tunnel_result** | **str** | Tunnel result | [optional] 
**tunnel_status** | **str** | Tunnel status | [optional] 
**vpn_cluster** | **str** | VPN cluster | [optional] 

## Example

```python
from scm_network_services.models.auto_vpn_monitor import AutoVpnMonitor

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnMonitor from a JSON string
auto_vpn_monitor_instance = AutoVpnMonitor.from_json(json)
# print the JSON string representation of the object
print(AutoVpnMonitor.to_json())

# convert the object into a dict
auto_vpn_monitor_dict = auto_vpn_monitor_instance.to_dict()
# create an instance of AutoVpnMonitor from a dict
auto_vpn_monitor_from_dict = AutoVpnMonitor.from_dict(auto_vpn_monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


