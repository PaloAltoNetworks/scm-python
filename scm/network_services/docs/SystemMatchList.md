# SystemMatchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the system match list entry | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**filter** | **str** | Filter of the system match list entry | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Name of the system match list entry | 
**send_email** | **List[str]** | Send Email List of the system match list entry | [optional] 
**send_http** | **List[str]** | Send HTTP List of the system match list entry | [optional] 
**send_snmptrap** | **List[str]** | Send SNMP Trap List of the system match list entry | [optional] 
**send_syslog** | **List[str]** | Send Sys Log List of the system match list entry | [optional] 
**send_to_panorama** | **bool** | Send to Panorama Flag of the system match list entry | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.network_services.models.system_match_list import SystemMatchList

# TODO update the JSON string below
json = "{}"
# create an instance of SystemMatchList from a JSON string
system_match_list_instance = SystemMatchList.from_json(json)
# print the JSON string representation of the object
print(SystemMatchList.to_json())

# convert the object into a dict
system_match_list_dict = system_match_list_instance.to_dict()
# create an instance of SystemMatchList from a dict
system_match_list_from_dict = SystemMatchList.from_dict(system_match_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


