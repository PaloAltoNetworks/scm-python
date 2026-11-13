# NgfirewallUpdateResponse

Response envelope returned by the Update Cloud NGFW firewall API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**NgfirewallUpdateResponseBody**](NgfirewallUpdateResponseBody.md) |  | [optional] 
**response_status** | [**NgfirewallResponseStatus**](NgfirewallResponseStatus.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_update_response import NgfirewallUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallUpdateResponse from a JSON string
ngfirewall_update_response_instance = NgfirewallUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(NgfirewallUpdateResponse.to_json())

# convert the object into a dict
ngfirewall_update_response_dict = ngfirewall_update_response_instance.to_dict()
# create an instance of NgfirewallUpdateResponse from a dict
ngfirewall_update_response_from_dict = NgfirewallUpdateResponse.from_dict(ngfirewall_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


