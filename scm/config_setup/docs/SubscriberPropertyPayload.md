# SubscriberPropertyPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**List[PropertyItem]**](PropertyItem.md) |  | [optional] 
**snippet_id** | **str** |  | 
**snippet_name** | **str** |  | 
**tsg_id** | **str** |  | 

## Example

```python
from scm_config_setup.models.subscriber_property_payload import SubscriberPropertyPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberPropertyPayload from a JSON string
subscriber_property_payload_instance = SubscriberPropertyPayload.from_json(json)
# print the JSON string representation of the object
print(SubscriberPropertyPayload.to_json())

# convert the object into a dict
subscriber_property_payload_dict = subscriber_property_payload_instance.to_dict()
# create an instance of SubscriberPropertyPayload from a dict
subscriber_property_payload_from_dict = SubscriberPropertyPayload.from_dict(subscriber_property_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


