# LoadConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional] 

## Example

```python
from scm.config_operations.models.load_config import LoadConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LoadConfig from a JSON string
load_config_instance = LoadConfig.from_json(json)
# print the JSON string representation of the object
print(LoadConfig.to_json())

# convert the object into a dict
load_config_dict = load_config_instance.to_dict()
# create an instance of LoadConfig from a dict
load_config_from_dict = LoadConfig.from_dict(load_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


