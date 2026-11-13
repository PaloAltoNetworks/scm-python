# Ngfirewalls

Cloud NGFW firewall schema. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**NgfirewallResponseBody**](NgfirewallResponseBody.md) |  | [optional] 
**response_status** | [**NgfirewallResponseStatus**](NgfirewallResponseStatus.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewalls import Ngfirewalls

# TODO update the JSON string below
json = "{}"
# create an instance of Ngfirewalls from a JSON string
ngfirewalls_instance = Ngfirewalls.from_json(json)
# print the JSON string representation of the object
print(Ngfirewalls.to_json())

# convert the object into a dict
ngfirewalls_dict = ngfirewalls_instance.to_dict()
# create an instance of Ngfirewalls from a dict
ngfirewalls_from_dict = Ngfirewalls.from_dict(ngfirewalls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


