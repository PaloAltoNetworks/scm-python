# LinkUnlinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**LinkUnlinkResult**](LinkUnlinkResult.md) |  | [optional] 
**response_status** | [**LinkResponseStatus**](LinkResponseStatus.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw_gcp.models.link_unlink_response import LinkUnlinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkUnlinkResponse from a JSON string
link_unlink_response_instance = LinkUnlinkResponse.from_json(json)
# print the JSON string representation of the object
print(LinkUnlinkResponse.to_json())

# convert the object into a dict
link_unlink_response_dict = link_unlink_response_instance.to_dict()
# create an instance of LinkUnlinkResponse from a dict
link_unlink_response_from_dict = LinkUnlinkResponse.from_dict(link_unlink_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


