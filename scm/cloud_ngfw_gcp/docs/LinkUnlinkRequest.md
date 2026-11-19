# LinkUnlinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The link code the firewall endpoint was created with, as returned by generate. | 
**gcp_tenant_id** | **str** | The Google Cloud tenant: organizations/{number}, projects/{project ID or number}, a bare number, or a bare project ID (6-30 characters: lowercase letters, digits and hyphens, starting with a letter and not ending with a hyphen).  | 

## Example

```python
from scm.cloud_ngfw_gcp.models.link_unlink_request import LinkUnlinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkUnlinkRequest from a JSON string
link_unlink_request_instance = LinkUnlinkRequest.from_json(json)
# print the JSON string representation of the object
print(LinkUnlinkRequest.to_json())

# convert the object into a dict
link_unlink_request_dict = link_unlink_request_instance.to_dict()
# create an instance of LinkUnlinkRequest from a dict
link_unlink_request_from_dict = LinkUnlinkRequest.from_dict(link_unlink_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


