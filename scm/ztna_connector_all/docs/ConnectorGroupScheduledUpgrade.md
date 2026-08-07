# ConnectorGroupScheduledUpgrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drain_timeout** | **int** | Drain timeout in seconds for rolling upgrades.  If omitted, defaults to 0. | [optional] 
**image_id** | **str** | The connector image version ID to upgrade to. | 
**rolling_upgrade** | **bool** | Whether to perform a rolling upgrade.  If omitted, defaults to false. Requires SaasAgent version 6.1.0 or later. | [optional] 
**scheduled_download** | **datetime** | The scheduled download time in RFC3339 format (UTC).  If omitted, defaults to current UTC time. | [optional] 
**scheduled_upgrade** | **datetime** | The scheduled upgrade time in RFC3339 format (UTC).  Must be after the scheduled_download time. If omitted, defaults to current UTC time. | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_group_scheduled_upgrade import ConnectorGroupScheduledUpgrade

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroupScheduledUpgrade from a JSON string
connector_group_scheduled_upgrade_instance = ConnectorGroupScheduledUpgrade.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroupScheduledUpgrade.to_json())

# convert the object into a dict
connector_group_scheduled_upgrade_dict = connector_group_scheduled_upgrade_instance.to_dict()
# create an instance of ConnectorGroupScheduledUpgrade from a dict
connector_group_scheduled_upgrade_from_dict = ConnectorGroupScheduledUpgrade.from_dict(connector_group_scheduled_upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


