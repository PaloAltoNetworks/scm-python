# DeletedSubscriber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** |  | [optional] 
**info** | [**SnippetShareInfo**](SnippetShareInfo.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from scm.config_setup.models.deleted_subscriber import DeletedSubscriber

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedSubscriber from a JSON string
deleted_subscriber_instance = DeletedSubscriber.from_json(json)
# print the JSON string representation of the object
print(DeletedSubscriber.to_json())

# convert the object into a dict
deleted_subscriber_dict = deleted_subscriber_instance.to_dict()
# create an instance of DeletedSubscriber from a dict
deleted_subscriber_from_dict = DeletedSubscriber.from_dict(deleted_subscriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


