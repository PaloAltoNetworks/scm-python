# ContentIdSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_id** | [**ContentIdSettingsContentId**](ContentIdSettingsContentId.md) |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_device_settings.models.content_id_settings import ContentIdSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ContentIdSettings from a JSON string
content_id_settings_instance = ContentIdSettings.from_json(json)
# print the JSON string representation of the object
print(ContentIdSettings.to_json())

# convert the object into a dict
content_id_settings_dict = content_id_settings_instance.to_dict()
# create an instance of ContentIdSettings from a dict
content_id_settings_from_dict = ContentIdSettings.from_dict(content_id_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


