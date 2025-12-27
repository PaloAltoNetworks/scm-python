# ZoneProtectionProfilesScanInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ZoneProtectionProfilesScanInnerAction**](ZoneProtectionProfilesScanInnerAction.md) |  | [optional] 
**interval** | **int** |  | [optional] 
**name** | **str** | The threat ID number.  These can be found in [Palo Alto Networks ThreatVault](https://threatvault.paloaltonetworks.com). * \&quot;8001\&quot; - TCP Port Scan * \&quot;8002\&quot; - Host Sweep * \&quot;8003\&quot; - UDP Port Scan * \&quot;8006\&quot; - Port Scan  | 
**threshold** | **int** |  | [optional] 

## Example

```python
from scm_network_services.models.zone_protection_profiles_scan_inner import ZoneProtectionProfilesScanInner

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfilesScanInner from a JSON string
zone_protection_profiles_scan_inner_instance = ZoneProtectionProfilesScanInner.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfilesScanInner.to_json())

# convert the object into a dict
zone_protection_profiles_scan_inner_dict = zone_protection_profiles_scan_inner_instance.to_dict()
# create an instance of ZoneProtectionProfilesScanInner from a dict
zone_protection_profiles_scan_inner_from_dict = ZoneProtectionProfilesScanInner.from_dict(zone_protection_profiles_scan_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


