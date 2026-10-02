# ConnectorStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cgnx_location** | **str** |  | [optional] 
**cgnx_scheduled_download** | **str** |  | [optional] 
**cgnx_scheduled_sw_version** | **str** |  | [optional] 
**cgnx_scheduled_upgrade** | **str** |  | [optional] 
**cgnx_sw_version** | **str** |  | [optional] 
**cgnx_upgrade_description** | **str** |  | [optional] 
**cgnx_upgrade_download_percent** | **float** |  | [optional] 
**cgnx_upgrade_failure_info** | **str** |  | [optional] 
**cgnx_upgrade_retry_count** | **float** |  | [optional] 
**cgnx_upgrade_state** | **str** | When undefined, no upgrade is in progress. | [optional] 
**cgnx_upgrade_status_last_updated** | **str** |  | [optional] 
**cgnx_vion_ip** | **str** |  | [optional] 
**cidr** | **str** |  | [optional] 
**error** | **object** |  | [optional] 
**flags** | [**ConnectorStatusFlags**](ConnectorStatusFlags.md) |  | [optional] 
**local_ip** | **str** |  | [optional] 
**sc_id** | **str** | Service Connection ID | [optional] 
**sc_name** | **str** |  | [optional] 
**state_bits** | **float** |  | [optional] 
**token_active** | **str** |  | [optional] 
**token_secret** | **str** |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.connector_status import ConnectorStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorStatus from a JSON string
connector_status_instance = ConnectorStatus.from_json(json)
# print the JSON string representation of the object
print(ConnectorStatus.to_json())

# convert the object into a dict
connector_status_dict = connector_status_instance.to_dict()
# create an instance of ConnectorStatus from a dict
connector_status_from_dict = ConnectorStatus.from_dict(connector_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


