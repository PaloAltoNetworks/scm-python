# ConnectorGroupUpgradeStatusDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_name** | **str** | Connector name | [optional] 
**connector_oid** | **str** | Connector ID | [optional] 
**current_sw_version** | **str** | Current software version running on the connector | [optional] 
**drain_time** | **int** | Time remaining until drain completes in seconds (present when connector is draining) | [optional] 
**failure_reason** | **str** | Reason for upgrade failure (if upgrade failed) | [optional] 
**sessions_count** | **int** | Number of active sessions (present when connector is draining) | [optional] 
**upgrade_status** | **str** | Current upgrade status of the connector | [optional] 
**upgrade_sw_version** | **str** | Target software version for the upgrade | [optional] 
**upgrade_time** | **str** | Scheduled upgrade time | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_group_upgrade_status_data_inner import ConnectorGroupUpgradeStatusDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroupUpgradeStatusDataInner from a JSON string
connector_group_upgrade_status_data_inner_instance = ConnectorGroupUpgradeStatusDataInner.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroupUpgradeStatusDataInner.to_json())

# convert the object into a dict
connector_group_upgrade_status_data_inner_dict = connector_group_upgrade_status_data_inner_instance.to_dict()
# create an instance of ConnectorGroupUpgradeStatusDataInner from a dict
connector_group_upgrade_status_data_inner_from_dict = ConnectorGroupUpgradeStatusDataInner.from_dict(connector_group_upgrade_status_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


