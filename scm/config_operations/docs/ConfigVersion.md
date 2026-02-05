# ConfigVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **str** | The administrator or service account that pushed this configuration version | 
**created** | **float** |  | 
**var_date** | **datetime** |  | 
**deleted** | **float** |  | 
**description** | **str** |  | 
**edited_by** | **str** |  | 
**id** | **int** | The configuration version | 
**impacted_devices** | **str** |  | 
**ngfw_scope** | **str** | A comma separated list of firewall serial numbers | [optional] 
**scope** | **str** |  | 
**swg_config** | **str** |  | [optional] 
**types** | **str** |  | 
**updated** | **float** |  | 
**version** | **str** | The configuration version name | 

## Example

```python
from scm.config_operations.models.config_version import ConfigVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigVersion from a JSON string
config_version_instance = ConfigVersion.from_json(json)
# print the JSON string representation of the object
print(ConfigVersion.to_json())

# convert the object into a dict
config_version_dict = config_version_instance.to_dict()
# create an instance of ConfigVersion from a dict
config_version_from_dict = ConfigVersion.from_dict(config_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


