# LinkUnlinkResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_tenant_id** | **str** | The Google Cloud tenant named in the request. | [optional] 
**unlinked** | **bool** | True whenever the request is accepted, including when there was nothing to retire. | [optional] 

## Example

```python
from scm.cloud_ngfw_gcp.models.link_unlink_result import LinkUnlinkResult

# TODO update the JSON string below
json = "{}"
# create an instance of LinkUnlinkResult from a JSON string
link_unlink_result_instance = LinkUnlinkResult.from_json(json)
# print the JSON string representation of the object
print(LinkUnlinkResult.to_json())

# convert the object into a dict
link_unlink_result_dict = link_unlink_result_instance.to_dict()
# create an instance of LinkUnlinkResult from a dict
link_unlink_result_from_dict = LinkUnlinkResult.from_dict(link_unlink_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


