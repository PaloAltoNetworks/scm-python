# NgfirewallNotification

A notification message associated with a firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_time** | **int** | Unix timestamp when this notification expires. | [optional] 
**id** | **str** | Unique identifier of the notification. | [optional] 
**link** | [**NgfirewallNotificationLink**](NgfirewallNotificationLink.md) |  | [optional] 
**msg** | **str** | The notification message text. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_notification import NgfirewallNotification

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallNotification from a JSON string
ngfirewall_notification_instance = NgfirewallNotification.from_json(json)
# print the JSON string representation of the object
print(NgfirewallNotification.to_json())

# convert the object into a dict
ngfirewall_notification_dict = ngfirewall_notification_instance.to_dict()
# create an instance of NgfirewallNotification from a dict
ngfirewall_notification_from_dict = NgfirewallNotification.from_dict(ngfirewall_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


