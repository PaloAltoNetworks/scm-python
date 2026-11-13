# NgfirewallNotificationLink

A hyperlink associated with a notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | The URL target of the link. | [optional] 
**text** | **str** | The display text of the link. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_notification_link import NgfirewallNotificationLink

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallNotificationLink from a JSON string
ngfirewall_notification_link_instance = NgfirewallNotificationLink.from_json(json)
# print the JSON string representation of the object
print(NgfirewallNotificationLink.to_json())

# convert the object into a dict
ngfirewall_notification_link_dict = ngfirewall_notification_link_instance.to_dict()
# create an instance of NgfirewallNotificationLink from a dict
ngfirewall_notification_link_from_dict = NgfirewallNotificationLink.from_dict(ngfirewall_notification_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


