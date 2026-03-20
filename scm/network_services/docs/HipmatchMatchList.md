# HipmatchMatchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the hipmatch match list entry | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**filter** | **str** | Filter of the hipmatch match list entry | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Name of the hipmatch match list entry | 
**quarantine** | **bool** | Quarantine Flag of the hipmatch match list entry | [optional] 
**send_email** | **List[str]** | Send Email List of the hipmatch match list entry | [optional] 
**send_http** | **List[str]** | Send HTTP List of the hipmatch match list entry | [optional] 
**send_snmptrap** | **List[str]** | Send SNMP Trap List of the hipmatch match list entry | [optional] 
**send_syslog** | **List[str]** | Send Sys Log List of the hipmatch match list entry | [optional] 
**send_to_panorama** | **bool** | Send to Panorama Flag of the hipmatch match list entry | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.network_services.models.hipmatch_match_list import HipmatchMatchList

# TODO update the JSON string below
json = "{}"
# create an instance of HipmatchMatchList from a JSON string
hipmatch_match_list_instance = HipmatchMatchList.from_json(json)
# print the JSON string representation of the object
print(HipmatchMatchList.to_json())

# convert the object into a dict
hipmatch_match_list_dict = hipmatch_match_list_instance.to_dict()
# create an instance of HipmatchMatchList from a dict
hipmatch_match_list_from_dict = HipmatchMatchList.from_dict(hipmatch_match_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


