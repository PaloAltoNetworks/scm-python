# IptagMatchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the iptag match list entry | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**filter** | **str** | Filter of the iptag match list entry | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Name of the iptag match list entry | 
**quarantine** | **bool** | Quarantine Flag of the iptag match list entry | [optional] 
**send_email** | **List[str]** | Send Email List of the iptag match list entry | [optional] 
**send_http** | **List[str]** | Send HTTP List of the iptag match list entry | [optional] 
**send_snmptrap** | **List[str]** | Send SNMP Trap List of the iptag match list entry | [optional] 
**send_syslog** | **List[str]** | Send Sys Log List of the iptag match list entry | [optional] 
**send_to_panorama** | **bool** | Send to Panorama Flag of the iptag match list entry | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.network_services.models.iptag_match_list import IptagMatchList

# TODO update the JSON string below
json = "{}"
# create an instance of IptagMatchList from a JSON string
iptag_match_list_instance = IptagMatchList.from_json(json)
# print the JSON string representation of the object
print(IptagMatchList.to_json())

# convert the object into a dict
iptag_match_list_dict = iptag_match_list_instance.to_dict()
# create an instance of IptagMatchList from a dict
iptag_match_list_from_dict = IptagMatchList.from_dict(iptag_match_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


