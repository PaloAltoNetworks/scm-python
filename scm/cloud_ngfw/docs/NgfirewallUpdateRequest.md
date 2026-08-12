# NgfirewallUpdateRequest

Request body for updating an existing Cloud NGFW firewall. Later will add more properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_name** | **str** | The name for the new Cloud NGFW firewall. | [optional] 
**id** | **str** | The ID of the Cloud NGFW firewall. | [optional] 
**region** | **str** | The AWS region where the Cloud NGFW firewall is deployed (e.g. us-east-1). | [optional] 
**tags** | [**List[NgfirewallTag]**](NgfirewallTag.md) | AWS resource tags to apply to the firewall. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_update_request import NgfirewallUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallUpdateRequest from a JSON string
ngfirewall_update_request_instance = NgfirewallUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(NgfirewallUpdateRequest.to_json())

# convert the object into a dict
ngfirewall_update_request_dict = ngfirewall_update_request_instance.to_dict()
# create an instance of NgfirewallUpdateRequest from a dict
ngfirewall_update_request_from_dict = NgfirewallUpdateRequest.from_dict(ngfirewall_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


