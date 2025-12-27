# HipObjectsFirewall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | [**HipObjectsDataLossPreventionCriteria**](HipObjectsDataLossPreventionCriteria.md) |  | [optional] 
**exclude_vendor** | **bool** |  | [optional] [default to False]
**vendor** | [**List[HipObjectsAntiMalwareVendorInner]**](HipObjectsAntiMalwareVendorInner.md) | Vendor name | [optional] 

## Example

```python
from scm_objects.models.hip_objects_firewall import HipObjectsFirewall

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsFirewall from a JSON string
hip_objects_firewall_instance = HipObjectsFirewall.from_json(json)
# print the JSON string representation of the object
print(HipObjectsFirewall.to_json())

# convert the object into a dict
hip_objects_firewall_dict = hip_objects_firewall_instance.to_dict()
# create an instance of HipObjectsFirewall from a dict
hip_objects_firewall_from_dict = HipObjectsFirewall.from_dict(hip_objects_firewall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


