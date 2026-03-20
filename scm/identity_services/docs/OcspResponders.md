# OcspResponders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**host_name** | **str** | The hostname or IP address of the OCSP server | 
**id** | **str** | The UUID of the OCSP responder profile | [readonly] 
**name** | **str** | The name of the OCSP responder profile | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.identity_services.models.ocsp_responders import OcspResponders

# TODO update the JSON string below
json = "{}"
# create an instance of OcspResponders from a JSON string
ocsp_responders_instance = OcspResponders.from_json(json)
# print the JSON string representation of the object
print(OcspResponders.to_json())

# convert the object into a dict
ocsp_responders_dict = ocsp_responders_instance.to_dict()
# create an instance of OcspResponders from a dict
ocsp_responders_from_dict = OcspResponders.from_dict(ocsp_responders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


