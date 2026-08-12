# NgfirewallResponseBody

Inner response object containing firewall details and operational status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall** | [**NgfirewallFirewall**](NgfirewallFirewall.md) |  | [optional] 
**status** | [**NgfirewallStatus**](NgfirewallStatus.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_response_body import NgfirewallResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallResponseBody from a JSON string
ngfirewall_response_body_instance = NgfirewallResponseBody.from_json(json)
# print the JSON string representation of the object
print(NgfirewallResponseBody.to_json())

# convert the object into a dict
ngfirewall_response_body_dict = ngfirewall_response_body_instance.to_dict()
# create an instance of NgfirewallResponseBody from a dict
ngfirewall_response_body_from_dict = NgfirewallResponseBody.from_dict(ngfirewall_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


