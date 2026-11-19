# LinkErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_status** | [**LinkResponseStatus**](LinkResponseStatus.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw_gcp.models.link_error_response import LinkErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkErrorResponse from a JSON string
link_error_response_instance = LinkErrorResponse.from_json(json)
# print the JSON string representation of the object
print(LinkErrorResponse.to_json())

# convert the object into a dict
link_error_response_dict = link_error_response_instance.to_dict()
# create an instance of LinkErrorResponse from a dict
link_error_response_from_dict = LinkErrorResponse.from_dict(link_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


