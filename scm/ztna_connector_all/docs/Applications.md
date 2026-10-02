# Applications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anycast_ip** | **str** | Anycast IP address assigned to this FQDN rule. | [optional] [readonly] 
**app_enabled** | **bool** | Whether the FQDN rule is enabled.  If omitted, defaults to false. | [optional] 
**created_time** | **str** |  | [optional] [readonly] 
**description** | **str** | The description of the resource | [optional] 
**group** | **str** | A comma separated list of connector group IDs | 
**icmp_allowed** | **bool** | Whether ICMP is allowed for this FQDN rule.  If omitted, defaults to true. | [optional] 
**name** | **str** | Name of the FQDN rule. | 
**oid** | **str** | The UUID of the resource | [optional] [readonly] 
**spec** | [**List[ApplicationsSpecInner]**](ApplicationsSpecInner.md) |  | 
**updated_time** | **str** |  | [optional] [readonly] 
**use_dc_ip** | **bool** | Whether to use datacenter IP for this FQDN rule.  If omitted, defaults to false. | [optional] 

## Example

```python
from scm.ztna_connector_all.models.applications import Applications

# TODO update the JSON string below
json = "{}"
# create an instance of Applications from a JSON string
applications_instance = Applications.from_json(json)
# print the JSON string representation of the object
print(Applications.to_json())

# convert the object into a dict
applications_dict = applications_instance.to_dict()
# create an instance of Applications from a dict
applications_from_dict = Applications.from_dict(applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


