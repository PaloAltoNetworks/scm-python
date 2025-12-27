# SessionTimeouts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**session_timeouts** | [**SessionTimeoutsSessionTimeouts**](SessionTimeoutsSessionTimeouts.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.device_settings.models.session_timeouts import SessionTimeouts

# TODO update the JSON string below
json = "{}"
# create an instance of SessionTimeouts from a JSON string
session_timeouts_instance = SessionTimeouts.from_json(json)
# print the JSON string representation of the object
print(SessionTimeouts.to_json())

# convert the object into a dict
session_timeouts_dict = session_timeouts_instance.to_dict()
# create an instance of SessionTimeouts from a dict
session_timeouts_from_dict = SessionTimeouts.from_dict(session_timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


