# LinkResponseStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | OK on success, otherwise an error code such as FIELD_MISSING or INTERNAL_ERROR. | [optional] 
**error_code** | **int** | 0 on success, non-zero on failure. | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from scm.cloud_ngfw_gcp.models.link_response_status import LinkResponseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LinkResponseStatus from a JSON string
link_response_status_instance = LinkResponseStatus.from_json(json)
# print the JSON string representation of the object
print(LinkResponseStatus.to_json())

# convert the object into a dict
link_response_status_dict = link_response_status_instance.to_dict()
# create an instance of LinkResponseStatus from a dict
link_response_status_from_dict = LinkResponseStatus.from_dict(link_response_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


