# Subnets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_enabled** | **bool** | Whether the IP subnet rule is enabled.  If omitted, defaults to false. | [optional] 
**created_time** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**group** | **str** | A comma separated list of connector group IDs | 
**icmp_allowed** | **bool** | Whether ICMP is allowed for this IP subnet rule.  If omitted, defaults to true. | [optional] 
**ip_subnets** | **str** | IPv4 subnet in CIDR notation (x.x.x.x/y) | 
**name** | **str** | Name of the IP Subnet rule.  It can only be 64 characters long and contain unicode text, space, dash, or underscore, or period. | 
**oid** | **str** | Id of the entry. | [optional] [readonly] 
**updated_time** | **str** |  | [optional] [readonly] 

## Example

```python
from scm.ztna_connector_all.models.subnets import Subnets

# TODO update the JSON string below
json = "{}"
# create an instance of Subnets from a JSON string
subnets_instance = Subnets.from_json(json)
# print the JSON string representation of the object
print(Subnets.to_json())

# convert the object into a dict
subnets_dict = subnets_instance.to_dict()
# create an instance of Subnets from a dict
subnets_from_dict = Subnets.from_dict(subnets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


