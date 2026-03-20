# RunningVersions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The timestamp of when the configuration version was pushed to the folder or firewall | 
**device** | **str** | The folder name or firewall serial number | 
**version** | **int** | The configuration version number | 

## Example

```python
from scm.config_operations.models.running_versions import RunningVersions

# TODO update the JSON string below
json = "{}"
# create an instance of RunningVersions from a JSON string
running_versions_instance = RunningVersions.from_json(json)
# print the JSON string representation of the object
print(RunningVersions.to_json())

# convert the object into a dict
running_versions_dict = running_versions_instance.to_dict()
# create an instance of RunningVersions from a dict
running_versions_from_dict = RunningVersions.from_dict(running_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


