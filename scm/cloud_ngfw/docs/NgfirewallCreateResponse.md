# NgfirewallCreateResponse

Response envelope returned by the Create Cloud NGFW firewall API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**NgfirewallCreateResponseBody**](NgfirewallCreateResponseBody.md) |  | [optional] 
**response_status** | [**NgfirewallResponseStatus**](NgfirewallResponseStatus.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_create_response import NgfirewallCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallCreateResponse from a JSON string
ngfirewall_create_response_instance = NgfirewallCreateResponse.from_json(json)
# print the JSON string representation of the object
print(NgfirewallCreateResponse.to_json())

# convert the object into a dict
ngfirewall_create_response_dict = ngfirewall_create_response_instance.to_dict()
# create an instance of NgfirewallCreateResponse from a dict
ngfirewall_create_response_from_dict = NgfirewallCreateResponse.from_dict(ngfirewall_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


