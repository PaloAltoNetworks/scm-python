# LinkGenerateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_tenant_id** | **str** | The Google Cloud tenant: organizations/{number}, projects/{project ID or number}, a bare number, or a bare project ID (6-30 characters: lowercase letters, digits and hyphens, starting with a letter and not ending with a hyphen).  | 

## Example

```python
from scm.cloud_ngfw_gcp.models.link_generate_request import LinkGenerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkGenerateRequest from a JSON string
link_generate_request_instance = LinkGenerateRequest.from_json(json)
# print the JSON string representation of the object
print(LinkGenerateRequest.to_json())

# convert the object into a dict
link_generate_request_dict = link_generate_request_instance.to_dict()
# create an instance of LinkGenerateRequest from a dict
link_generate_request_from_dict = LinkGenerateRequest.from_dict(link_generate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


