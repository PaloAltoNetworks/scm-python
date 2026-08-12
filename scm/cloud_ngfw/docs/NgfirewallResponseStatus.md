# NgfirewallResponseStatus

API-level response metadata at the top level of the envelope.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** | Non-zero error code if the API request failed. | [optional] 
**reason** | **str** | Human-readable reason for the error, if any. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_response_status import NgfirewallResponseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallResponseStatus from a JSON string
ngfirewall_response_status_instance = NgfirewallResponseStatus.from_json(json)
# print the JSON string representation of the object
print(NgfirewallResponseStatus.to_json())

# convert the object into a dict
ngfirewall_response_status_dict = ngfirewall_response_status_instance.to_dict()
# create an instance of NgfirewallResponseStatus from a dict
ngfirewall_response_status_from_dict = NgfirewallResponseStatus.from_dict(ngfirewall_response_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


