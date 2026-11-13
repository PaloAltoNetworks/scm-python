# NgfirewallsListResponse

Response envelope for the List Cloud NGFW firewalls API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**NgfirewallsListResponseBody**](NgfirewallsListResponseBody.md) |  | [optional] 
**response_status** | [**NgfirewallResponseStatus**](NgfirewallResponseStatus.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewalls_list_response import NgfirewallsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallsListResponse from a JSON string
ngfirewalls_list_response_instance = NgfirewallsListResponse.from_json(json)
# print the JSON string representation of the object
print(NgfirewallsListResponse.to_json())

# convert the object into a dict
ngfirewalls_list_response_dict = ngfirewalls_list_response_instance.to_dict()
# create an instance of NgfirewallsListResponse from a dict
ngfirewalls_list_response_from_dict = NgfirewallsListResponse.from_dict(ngfirewalls_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


