# Wildcards


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_enabled** | **bool** | Whether the wildcard is enabled.  If omitted, defaults to false. | [optional] 
**applications** | **object** | Discovered Wildcard App oid to name mapping. | [optional] [readonly] 
**created_time** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**enable_policy** | **bool** | Whether policy is enabled for this wildcard.  If omitted, defaults to false. | [optional] 
**fqdn** | **str** | The wildcard to match. | 
**group** | **str** | A comma separated list of connector group IDs | 
**icmp_allowed** | **bool** | Whether ICMP is allowed for this wildcard.  If omitted, defaults to true. | [optional] 
**id** | **str** | Id of the entry as returned by list/get operations. | [optional] [readonly] 
**name** | **str** | Name of the wildcard.  It can only be 64 characters long and contain unicode text, space, dash, or underscore, or period. | 
**oid** | **str** | Id of the entry. | [optional] [readonly] 
**probe_port** | **str** | The probing port if the &#x60;probe_type&#x60; is &#x60;tcp_ping&#x60;. | [optional] 
**probe_type** | **str** | The probing type.  The value can be &#x60;tcp_ping&#x60;, &#x60;icmp_ping&#x60;, or omitted. | [optional] 
**tcp_port** | **str** | TCP port number(s).  It can be a single port number, multiple port numbers separated by comma, or a port range like 8000-9000.  If both tcp_port and udp_port are omitted, tcp_port defaults to 443. | [optional] 
**udp_port** | **str** | UDP port number(s).  It can be a single port number, multiple port numbers separated by comma, or a port range like 8000-9000.  If both tcp_port and udp_port are omitted, tcp_port defaults to 443. | [optional] 
**updated_time** | **str** |  | [optional] [readonly] 
**use_dc_ip** | **bool** | Whether to use datacenter IP for this wildcard.  If omitted, defaults to false. | [optional] 

## Example

```python
from scm.ztna_connector_all.models.wildcards import Wildcards

# TODO update the JSON string below
json = "{}"
# create an instance of Wildcards from a JSON string
wildcards_instance = Wildcards.from_json(json)
# print the JSON string representation of the object
print(Wildcards.to_json())

# convert the object into a dict
wildcards_dict = wildcards_instance.to_dict()
# create an instance of Wildcards from a dict
wildcards_from_dict = Wildcards.from_dict(wildcards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


