# ApplicationsSpecInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | FQDN of the rule. | 
**probe_port** | **str** | The probing port if the &#x60;probe_type&#x60; is &#x60;tcp_ping&#x60;. | [optional] 
**probe_type** | **str** | The probing type.  The value can be &#x60;tcp_ping&#x60;, &#x60;icmp_ping&#x60;, or omitted. | [optional] 
**tcp_port** | **str** | TCP port number(s).  It can be a single port number, multiple port numbers separated by comma, or a port range like 8000-9000.  If both tcp_port and udp_port are omitted, tcp_port defaults to 443. | [optional] 
**udp_port** | **str** | UDP port number(s).  It can be a single port number, multiple port numbers separated by comma, or a port range like 8000-9000.  If both tcp_port and udp_port are omitted, tcp_port defaults to 443. | [optional] 

## Example

```python
from scm.ztna_connector_all.models.applications_spec_inner import ApplicationsSpecInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsSpecInner from a JSON string
applications_spec_inner_instance = ApplicationsSpecInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationsSpecInner.to_json())

# convert the object into a dict
applications_spec_inner_dict = applications_spec_inner_instance.to_dict()
# create an instance of ApplicationsSpecInner from a dict
applications_spec_inner_from_dict = ApplicationsSpecInner.from_dict(applications_spec_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


