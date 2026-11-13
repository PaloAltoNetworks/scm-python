# NgfirewallEndpointPrefixes

IP prefix lists associated with a firewall endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_prefix** | [**NgfirewallPrefixList**](NgfirewallPrefixList.md) |  | [optional] 
**public_prefix** | [**NgfirewallPrefixList**](NgfirewallPrefixList.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_endpoint_prefixes import NgfirewallEndpointPrefixes

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallEndpointPrefixes from a JSON string
ngfirewall_endpoint_prefixes_instance = NgfirewallEndpointPrefixes.from_json(json)
# print the JSON string representation of the object
print(NgfirewallEndpointPrefixes.to_json())

# convert the object into a dict
ngfirewall_endpoint_prefixes_dict = ngfirewall_endpoint_prefixes_instance.to_dict()
# create an instance of NgfirewallEndpointPrefixes from a dict
ngfirewall_endpoint_prefixes_from_dict = NgfirewallEndpointPrefixes.from_dict(ngfirewall_endpoint_prefixes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


