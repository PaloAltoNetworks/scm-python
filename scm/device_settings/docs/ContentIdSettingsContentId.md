# ContentIdSettingsContentId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_forward_decrypted_content** | **bool** |  | [optional] [default to False]
**allow_http_range** | **bool** |  | [optional] [default to True]
**application** | [**ContentIdSettingsContentIdApplication**](ContentIdSettingsContentIdApplication.md) |  | [optional] 
**extended_capture_segment** | **int** |  | [optional] [default to 5]
**strip_x_fwd_for** | **bool** |  | [optional] [default to False]
**tcp_bypass_exceed_queue** | **bool** |  | [optional] [default to True]
**udp_bypass_exceed_queue** | **bool** |  | [optional] [default to True]
**x_forwarded_for** | **str** |  | [optional] [default to '0']

## Example

```python
from scm_device_settings.models.content_id_settings_content_id import ContentIdSettingsContentId

# TODO update the JSON string below
json = "{}"
# create an instance of ContentIdSettingsContentId from a JSON string
content_id_settings_content_id_instance = ContentIdSettingsContentId.from_json(json)
# print the JSON string representation of the object
print(ContentIdSettingsContentId.to_json())

# convert the object into a dict
content_id_settings_content_id_dict = content_id_settings_content_id_instance.to_dict()
# create an instance of ContentIdSettingsContentId from a dict
content_id_settings_content_id_from_dict = ContentIdSettingsContentId.from_dict(content_id_settings_content_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


