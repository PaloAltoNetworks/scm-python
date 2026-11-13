# DiagnosticFileListDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**filename** | **str** | Name of the file. | [optional] 
**filesize** | **float** | Size of the file. | [optional] 
**id** | **str** | Request id | [optional] 
**state** | **str** | stopped, complete, inprogress | [optional] 

## Example

```python
from scm.ztna_connector_all.models.diagnostic_file_list_data_inner import DiagnosticFileListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticFileListDataInner from a JSON string
diagnostic_file_list_data_inner_instance = DiagnosticFileListDataInner.from_json(json)
# print the JSON string representation of the object
print(DiagnosticFileListDataInner.to_json())

# convert the object into a dict
diagnostic_file_list_data_inner_dict = diagnostic_file_list_data_inner_instance.to_dict()
# create an instance of DiagnosticFileListDataInner from a dict
diagnostic_file_list_data_inner_from_dict = DiagnosticFileListDataInner.from_dict(diagnostic_file_list_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


