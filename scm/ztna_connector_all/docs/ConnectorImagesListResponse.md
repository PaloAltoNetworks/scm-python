# ConnectorImagesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConnectorImages]**](ConnectorImages.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.ztna_connector_all.models.connector_images_list_response import ConnectorImagesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorImagesListResponse from a JSON string
connector_images_list_response_instance = ConnectorImagesListResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectorImagesListResponse.to_json())

# convert the object into a dict
connector_images_list_response_dict = connector_images_list_response_instance.to_dict()
# create an instance of ConnectorImagesListResponse from a dict
connector_images_list_response_from_dict = ConnectorImagesListResponse.from_dict(connector_images_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


