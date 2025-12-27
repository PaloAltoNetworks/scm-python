# Services


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the service | [optional] [readonly] 
**name** | **str** | The name of the service | 
**protocol** | [**ServicesProtocol**](ServicesProtocol.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**tag** | **List[str]** | Tags for service object | [optional] 

## Example

```python
from scm.objects.models.services import Services

# TODO update the JSON string below
json = "{}"
# create an instance of Services from a JSON string
services_instance = Services.from_json(json)
# print the JSON string representation of the object
print(Services.to_json())

# convert the object into a dict
services_dict = services_instance.to_dict()
# create an instance of Services from a dict
services_from_dict = Services.from_dict(services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


