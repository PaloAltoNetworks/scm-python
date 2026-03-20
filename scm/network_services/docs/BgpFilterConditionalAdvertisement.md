# BgpFilterConditionalAdvertisement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exist** | [**BgpFilterConditionalAdvertisementExist**](BgpFilterConditionalAdvertisementExist.md) |  | [optional] 
**non_exist** | [**BgpFilterConditionalAdvertisementNonExist**](BgpFilterConditionalAdvertisementNonExist.md) |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_filter_conditional_advertisement import BgpFilterConditionalAdvertisement

# TODO update the JSON string below
json = "{}"
# create an instance of BgpFilterConditionalAdvertisement from a JSON string
bgp_filter_conditional_advertisement_instance = BgpFilterConditionalAdvertisement.from_json(json)
# print the JSON string representation of the object
print(BgpFilterConditionalAdvertisement.to_json())

# convert the object into a dict
bgp_filter_conditional_advertisement_dict = bgp_filter_conditional_advertisement_instance.to_dict()
# create an instance of BgpFilterConditionalAdvertisement from a dict
bgp_filter_conditional_advertisement_from_dict = BgpFilterConditionalAdvertisement.from_dict(bgp_filter_conditional_advertisement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


