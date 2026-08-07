# AdjustTcpMss

TCP MSS adjustment settings for the interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable TCP MSS adjustment on the interface | [optional] 
**ipv4_mss_adjustment** | **int** | IPv4 MSS adjustment size in bytes | [optional] 
**ipv6_mss_adjustment** | **int** | IPv6 MSS adjustment size in bytes | [optional] 

## Example

```python
from scm.network_services.models.adjust_tcp_mss import AdjustTcpMss

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustTcpMss from a JSON string
adjust_tcp_mss_instance = AdjustTcpMss.from_json(json)
# print the JSON string representation of the object
print(AdjustTcpMss.to_json())

# convert the object into a dict
adjust_tcp_mss_dict = adjust_tcp_mss_instance.to_dict()
# create an instance of AdjustTcpMss from a dict
adjust_tcp_mss_from_dict = AdjustTcpMss.from_dict(adjust_tcp_mss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


