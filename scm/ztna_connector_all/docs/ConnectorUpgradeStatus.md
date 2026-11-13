# ConnectorUpgradeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_image_id** | **str** | Currently active image ID | [optional] 
**active_version** | **str** | Currently active software version | [optional] 
**download_percent** | **int** | Download progress percentage | [optional] 
**failure_info** | **str** | Failure information if upgrade failed | [optional] 
**previous_image_id** | **str** | Previous image ID | [optional] 
**scheduled_download** | **str** | Scheduled download time | [optional] 
**scheduled_upgrade** | **str** | Scheduled upgrade time | [optional] 
**upgrade_description** | **str** | Description of the upgrade | [optional] 
**upgrade_image_id** | **str** | Target upgrade image ID | [optional] 
**upgrade_state** | **str** | Current state of the upgrade process | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_upgrade_status import ConnectorUpgradeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorUpgradeStatus from a JSON string
connector_upgrade_status_instance = ConnectorUpgradeStatus.from_json(json)
# print the JSON string representation of the object
print(ConnectorUpgradeStatus.to_json())

# convert the object into a dict
connector_upgrade_status_dict = connector_upgrade_status_instance.to_dict()
# create an instance of ConnectorUpgradeStatus from a dict
connector_upgrade_status_from_dict = ConnectorUpgradeStatus.from_dict(connector_upgrade_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


