# ContentIdSettingsContentIdApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass_exceed_queue** | **bool** |  | [optional] [default to False]

## Example

```python
from scm.device_settings.models.content_id_settings_content_id_application import ContentIdSettingsContentIdApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ContentIdSettingsContentIdApplication from a JSON string
content_id_settings_content_id_application_instance = ContentIdSettingsContentIdApplication.from_json(json)
# print the JSON string representation of the object
print(ContentIdSettingsContentIdApplication.to_json())

# convert the object into a dict
content_id_settings_content_id_application_dict = content_id_settings_content_id_application_instance.to_dict()
# create an instance of ContentIdSettingsContentIdApplication from a dict
content_id_settings_content_id_application_from_dict = ContentIdSettingsContentIdApplication.from_dict(content_id_settings_content_id_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


