# NgfirewallEndpoint

Configuration and status of a single firewall VPC endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The AWS account ID that owns this endpoint. | [optional] 
**egress_nat_enabled** | **bool** | Whether egress NAT is enabled for this endpoint. | [optional] 
**endpoint_id** | **str** | The VPC endpoint ID. | [optional] 
**mode** | **str** | The endpoint management mode. | [optional] 
**prefixes** | [**NgfirewallEndpointPrefixes**](NgfirewallEndpointPrefixes.md) |  | [optional] 
**rejected_reason** | **str** | Human-readable reason if the endpoint was rejected. | [optional] 
**status** | **str** | The current provisioning status of the endpoint. | [optional] 
**subnet_id** | **str** | The AWS subnet ID in which the endpoint resides. | [optional] 
**vpc_id** | **str** | The AWS VPC ID in which the endpoint resides. | [optional] 
**zone_id** | **str** | The availability zone ID for this endpoint. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_endpoint import NgfirewallEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallEndpoint from a JSON string
ngfirewall_endpoint_instance = NgfirewallEndpoint.from_json(json)
# print the JSON string representation of the object
print(NgfirewallEndpoint.to_json())

# convert the object into a dict
ngfirewall_endpoint_dict = ngfirewall_endpoint_instance.to_dict()
# create an instance of NgfirewallEndpoint from a dict
ngfirewall_endpoint_from_dict = NgfirewallEndpoint.from_dict(ngfirewall_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


