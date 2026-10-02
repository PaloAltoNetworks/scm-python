# DiagnosticFileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DiagnosticFileListDataInner]**](DiagnosticFileListDataInner.md) |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.diagnostic_file_list import DiagnosticFileList

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticFileList from a JSON string
diagnostic_file_list_instance = DiagnosticFileList.from_json(json)
# print the JSON string representation of the object
print(DiagnosticFileList.to_json())

# convert the object into a dict
diagnostic_file_list_dict = diagnostic_file_list_instance.to_dict()
# create an instance of DiagnosticFileList from a dict
diagnostic_file_list_from_dict = DiagnosticFileList.from_dict(diagnostic_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


