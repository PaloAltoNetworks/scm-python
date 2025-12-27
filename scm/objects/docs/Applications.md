# Applications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**able_to_transfer_file** | **bool** |  | [optional] 
**alg_disable_capability** | **str** |  | [optional] 
**category** | **str** |  | 
**consume_big_bandwidth** | **bool** |  | [optional] 
**data_ident** | **bool** |  | [optional] 
**default** | [**ApplicationsDefault**](ApplicationsDefault.md) |  | [optional] 
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**evasive_behavior** | **bool** |  | [optional] 
**file_type_ident** | **bool** |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**has_known_vulnerability** | **bool** |  | [optional] 
**id** | **str** | The UUID of the application | [optional] [readonly] 
**name** | **str** | The name of the application | 
**no_appid_caching** | **bool** |  | [optional] 
**parent_app** | **str** |  | [optional] 
**pervasive_use** | **bool** |  | [optional] 
**prone_to_misuse** | **bool** |  | [optional] 
**risk** | **object** |  | 
**signature** | [**List[ApplicationsSignatureInner]**](ApplicationsSignatureInner.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**subcategory** | **str** |  | [optional] 
**tcp_half_closed_timeout** | **int** | timeout for half-close session in seconds | [optional] 
**tcp_time_wait_timeout** | **int** | timeout for session in time_wait state in seconds | [optional] 
**tcp_timeout** | **int** | timeout in seconds | [optional] 
**technology** | **str** |  | [optional] 
**timeout** | **int** | timeout in seconds | [optional] 
**tunnel_applications** | **bool** |  | [optional] 
**tunnel_other_application** | **bool** |  | [optional] 
**udp_timeout** | **int** | timeout in seconds | [optional] 
**used_by_malware** | **bool** |  | [optional] 
**virus_ident** | **bool** |  | [optional] 

## Example

```python
from scm_objects.models.applications import Applications

# TODO update the JSON string below
json = "{}"
# create an instance of Applications from a JSON string
applications_instance = Applications.from_json(json)
# print the JSON string representation of the object
print(Applications.to_json())

# convert the object into a dict
applications_dict = applications_instance.to_dict()
# create an instance of Applications from a dict
applications_from_dict = Applications.from_dict(applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


