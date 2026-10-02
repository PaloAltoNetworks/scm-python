# ConnectorGroupUpgradeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConnectorGroupUpgradeStatusDataInner]**](ConnectorGroupUpgradeStatusDataInner.md) | List of connector upgrade statuses within this group | [optional] 
**name** | **str** | Connector group name | [optional] 
**oid** | **str** | Connector group ID | [optional] 
**rolling_upgrade** | **bool** | Whether rolling upgrade is enabled for this connector group | [optional] 
**upgrade_status** | **str** | Overall upgrade status for the connector group | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_group_upgrade_status import ConnectorGroupUpgradeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorGroupUpgradeStatus from a JSON string
connector_group_upgrade_status_instance = ConnectorGroupUpgradeStatus.from_json(json)
# print the JSON string representation of the object
print(ConnectorGroupUpgradeStatus.to_json())

# convert the object into a dict
connector_group_upgrade_status_dict = connector_group_upgrade_status_instance.to_dict()
# create an instance of ConnectorGroupUpgradeStatus from a dict
connector_group_upgrade_status_from_dict = ConnectorGroupUpgradeStatus.from_dict(connector_group_upgrade_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


