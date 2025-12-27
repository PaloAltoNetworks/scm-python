# AddSubscriberRequestPayloadInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snippet_id** | **str** |  | 
**snippet_name** | **str** |  | 
**tsg_id** | **str** |  | 

## Example

```python
from scm_config_setup.models.add_subscriber_request_payload_inner import AddSubscriberRequestPayloadInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddSubscriberRequestPayloadInner from a JSON string
add_subscriber_request_payload_inner_instance = AddSubscriberRequestPayloadInner.from_json(json)
# print the JSON string representation of the object
print(AddSubscriberRequestPayloadInner.to_json())

# convert the object into a dict
add_subscriber_request_payload_inner_dict = add_subscriber_request_payload_inner_instance.to_dict()
# create an instance of AddSubscriberRequestPayloadInner from a dict
add_subscriber_request_payload_inner_from_dict = AddSubscriberRequestPayloadInner.from_dict(add_subscriber_request_payload_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


