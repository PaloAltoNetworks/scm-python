# LinkGenerateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**LinkGenerateResult**](LinkGenerateResult.md) |  | [optional] 
**response_status** | [**LinkResponseStatus**](LinkResponseStatus.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw_gcp.models.link_generate_response import LinkGenerateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkGenerateResponse from a JSON string
link_generate_response_instance = LinkGenerateResponse.from_json(json)
# print the JSON string representation of the object
print(LinkGenerateResponse.to_json())

# convert the object into a dict
link_generate_response_dict = link_generate_response_instance.to_dict()
# create an instance of LinkGenerateResponse from a dict
link_generate_response_from_dict = LinkGenerateResponse.from_dict(link_generate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


