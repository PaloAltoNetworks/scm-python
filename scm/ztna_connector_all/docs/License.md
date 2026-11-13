# License


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | **float** |  | [optional] 
**connectors** | **float** |  | [optional] 
**expiry** | **date** |  | [optional] 
**license_name** | **str** |  | [optional] 
**max_applications** | **float** |  | [optional] 
**max_connectors** | **float** |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.license import License

# TODO update the JSON string below
json = "{}"
# create an instance of License from a JSON string
license_instance = License.from_json(json)
# print the JSON string representation of the object
print(License.to_json())

# convert the object into a dict
license_dict = license_instance.to_dict()
# create an instance of License from a dict
license_from_dict = License.from_dict(license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


