# NgfirewallsListResponseBody

Inner response body containing the firewall list and pagination token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewalls** | [**List[NgfirewallSummary]**](NgfirewallSummary.md) | List of firewall summaries (present when describe is not requested). | [optional] 
**firewalls_describe** | [**List[NgfirewallResponseBody]**](NgfirewallResponseBody.md) | List of detailed firewall descriptions (present when describe is requested). | [optional] 
**next_token** | **str** | Pagination token to retrieve the next page of results. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewalls_list_response_body import NgfirewallsListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallsListResponseBody from a JSON string
ngfirewalls_list_response_body_instance = NgfirewallsListResponseBody.from_json(json)
# print the JSON string representation of the object
print(NgfirewallsListResponseBody.to_json())

# convert the object into a dict
ngfirewalls_list_response_body_dict = ngfirewalls_list_response_body_instance.to_dict()
# create an instance of NgfirewallsListResponseBody from a dict
ngfirewalls_list_response_body_from_dict = NgfirewallsListResponseBody.from_dict(ngfirewalls_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


