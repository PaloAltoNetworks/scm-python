# ConnectorScheduledUpgrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** | The connector image version ID to upgrade to. | 
**scheduled_download** | **datetime** | The scheduled download time in RFC3339 format (UTC).  If omitted, defaults to current UTC time. | [optional] 
**scheduled_upgrade** | **datetime** | The scheduled upgrade time in RFC3339 format (UTC).  Must be after the scheduled_download time. If omitted, defaults to current UTC time. | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_scheduled_upgrade import ConnectorScheduledUpgrade

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorScheduledUpgrade from a JSON string
connector_scheduled_upgrade_instance = ConnectorScheduledUpgrade.from_json(json)
# print the JSON string representation of the object
print(ConnectorScheduledUpgrade.to_json())

# convert the object into a dict
connector_scheduled_upgrade_dict = connector_scheduled_upgrade_instance.to_dict()
# create an instance of ConnectorScheduledUpgrade from a dict
connector_scheduled_upgrade_from_dict = ConnectorScheduledUpgrade.from_dict(connector_scheduled_upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


