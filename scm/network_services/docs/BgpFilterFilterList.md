# BgpFilterFilterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound** | **str** |  | [optional] 
**outbound** | **str** |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_filter_filter_list import BgpFilterFilterList

# TODO update the JSON string below
json = "{}"
# create an instance of BgpFilterFilterList from a JSON string
bgp_filter_filter_list_instance = BgpFilterFilterList.from_json(json)
# print the JSON string representation of the object
print(BgpFilterFilterList.to_json())

# convert the object into a dict
bgp_filter_filter_list_dict = bgp_filter_filter_list_instance.to_dict()
# create an instance of BgpFilterFilterList from a dict
bgp_filter_filter_list_from_dict = BgpFilterFilterList.from_dict(bgp_filter_filter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


